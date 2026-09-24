<?php

declare(strict_types=1);

const PUBLISHER_NAME = 'Village Link Type 2 publisher';

function respond(int $status, string $title, string $body): never
{
    http_response_code($status);
    header('Content-Type: text/html; charset=utf-8');
    header('X-Content-Type-Options: nosniff');
    header('Cache-Control: no-store');

    if (($_SERVER['REQUEST_METHOD'] ?? 'GET') === 'HEAD') {
        exit;
    }

    $safeTitle = htmlspecialchars($title, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    echo "<!doctype html>\n<html lang=\"en\">\n<meta charset=\"utf-8\">\n";
    echo '<meta name="viewport" content="width=device-width, initial-scale=1">';
    echo "<title>{$safeTitle}</title>\n";
    echo '<main style="max-width:52rem;margin:3rem auto;padding:0 1rem;font:1rem/1.5 system-ui,sans-serif">';
    echo "<h1>{$safeTitle}</h1>\n{$body}</main>\n";
    exit;
}

function h(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($method !== 'GET' && $method !== 'HEAD') {
    header('Allow: GET, HEAD');
    respond(405, 'Method not allowed', '<p>This publisher supports GET and HEAD.</p>');
}

$documentRoot = (string) ($_SERVER['DOCUMENT_ROOT'] ?? __DIR__);
$defaultConfigPath = dirname(dirname($documentRoot)) . '/vl2-config.php';
$configPath = getenv('VL2_CONFIG_PATH') ?: $defaultConfigPath;

if (!is_file($configPath)) {
    respond(503, 'Publisher unavailable', '<p>The private database configuration is not installed.</p>');
}

$config = require $configPath;
if (!is_array($config)) {
    respond(503, 'Publisher unavailable', '<p>The private database configuration is invalid.</p>');
}

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

try {
    $db = new mysqli(
        (string) ($config['host'] ?? 'localhost'),
        (string) ($config['user'] ?? ''),
        (string) ($config['password'] ?? ''),
        (string) ($config['database'] ?? ''),
    );
    $db->set_charset('utf8mb4');
} catch (Throwable $error) {
    error_log(PUBLISHER_NAME . ': ' . $error->getMessage());
    respond(503, 'Publisher unavailable', '<p>The backing store could not be reached.</p>');
}

$requestUri = (string) ($_SERVER['REQUEST_URI'] ?? '/');
$path = (string) (parse_url($requestUri, PHP_URL_PATH) ?? '/');

if ($path === '/' || $path === '') {
    $result = $db->query(
        'SELECT r.serialized_value, a.endpoint_uri AS endpoint_a, b.endpoint_uri AS endpoint_b '
        . 'FROM representations AS r '
        . 'JOIN links AS l ON l.link_id = r.link_id '
        . 'JOIN endpoints AS a ON a.endpoint_id = l.endpoint_a_id '
        . 'JOIN endpoints AS b ON b.endpoint_id = l.endpoint_b_id '
        . 'ORDER BY r.representation_id'
    );

    $items = '';
    while ($row = $result->fetch_assoc()) {
        $items .= '<li><a href="' . h((string) $row['serialized_value']) . '">'
            . h((string) $row['endpoint_a']) . ' ↔ ' . h((string) $row['endpoint_b'])
            . '</a></li>';
    }

    respond(200, PUBLISHER_NAME, $items === '' ? '<p>No representations published.</p>' : "<ul>{$items}</ul>");
}

$candidate = 'https://wab.inky.tech/' . ltrim($path, '/');
$statement = $db->prepare(
    'SELECT r.representation_id, r.serialized_value, e.encoding_name, e.encoding_version, '
    . 'a.endpoint_uri AS endpoint_a, b.endpoint_uri AS endpoint_b '
    . 'FROM representations AS r '
    . 'JOIN links AS l ON l.link_id = r.link_id '
    . 'JOIN endpoints AS a ON a.endpoint_id = l.endpoint_a_id '
    . 'JOIN endpoints AS b ON b.endpoint_id = l.endpoint_b_id '
    . 'JOIN encodings AS e ON e.encoding_id = r.encoding_id '
    . 'WHERE r.serialized_value = ? LIMIT 1'
);
$statement->bind_param('s', $candidate);
$statement->execute();
$row = $statement->get_result()->fetch_assoc();

if ($row === null) {
    respond(404, 'Village Link not found', '<p>No representation matches this exact URI.</p>');
}

$body = '<dl>'
    . '<dt>Endpoint A</dt><dd><a href="' . h((string) $row['endpoint_a']) . '">' . h((string) $row['endpoint_a']) . '</a></dd>'
    . '<dt>Endpoint B</dt><dd><a href="' . h((string) $row['endpoint_b']) . '">' . h((string) $row['endpoint_b']) . '</a></dd>'
    . '<dt>Encoding</dt><dd>' . h((string) $row['encoding_name']) . ' ' . h((string) $row['encoding_version']) . '</dd>'
    . '<dt>Published W</dt><dd><code>' . h((string) $row['serialized_value']) . '</code></dd>'
    . '</dl>';

respond(200, 'Village Link representation', $body);
