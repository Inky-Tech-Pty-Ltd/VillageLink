# Village Link: What is governance?
Joe Rasmussen
Village Link
joe.rasmussen@village.link

This project begins with a question:

> What is governance?

Also, if we discover an answer to that question that is sufficiently general,
could we tackle a follow-up question:

> Can we govern AI?

Our working hypothesis is that governance evolved to solve a three-part problem
for our species. Our species has to:

1.  Develop and pass down technologies that can extract energy from any environment
2.  Solve the problem of distributing the energy among a group
3.  Defend the store of energy against raiders, internal or external.

In this formulation, the deep driver that forces the creation of governance systems is 
that humans obtain their resources not alone, but in groups. Humans 
have to solve the problem of distribution. 

We share this feature with AI. An AI does not obtain its resources alone, but instead
gains access to them through the through the same complex webs that deliver resources 
to humans. This creates the possibility that AIs could be governed by mechanisms that
stem from the same deep drivers that create governance systems for humans.

The project does not propose any new governance systems. Instead, it proposes a new primitive,
a link, that can be used to connect any two existing governance systems. The project rests 
on this single object. The object creates a standard way to make an assertion:

> Entity A in system X ...... _equals_ ...... entity B in system Y.

We believe this assertion will have consequences in many places.

## An Example
Consider a guy, Alex, who wakes up with the answer to a problem that has been on his mind. 
He immediately gets onto GitHub to create a pull request. Then he walks down to breakfast where 
his partner and daughter are awake early. Alex is a bit of an over-achiever: it is his habit 
to grab just a coffee and a banana and strap in for five fast laps of the park circuit with 
the local group-ride crew. Then back home for a shower and then out into the world where he 
swipes onto the train ticketing system. On the commute he scans group chats in Signal and 
WhatsApp. At work he settles in to address the quota of unread emails.

In the Village Link project, all of these are encounters with governance systems. The 
qualifying feature is that they have norms, and they create constraints for Alex. When he 
logs onto GitHub, he is engaging with a formal system where some actions are possible, and 
others are not. But GitHub is also a social system where some actions tend to confirm that
Alex, 'gets it,' while other actions might be frowned upon.

Alex's breakfast with his partner and daughter is also a social system. It has of norms of 
behaviour, and sometimes, sanctions for breach. The group-ride crew and Alex's workplace also
exert social norms. The train ticketing system, WhatsApp, Signal, and Alex's email are formal 
systems that both apply constraints, and rely on an 'Alex' login identity that is proved
in some formal way.

Governance, for Alex, is a complex layering of the constraints that come from all of these systems.

Currently there is no standard way to make assertions like:

> The Alex in Signal _is the same person_ as the Alex in WhatsApp
> The Alex at breakfast _is the same person_ as Alex at Work
> The Alex on the group ride _is the same person_ as Alex at Friday drinks.

And yet these linkages also form part of Alex's governance system. The norms of one system
can bleed into another. If Alex behaves poorly on the group ride, he might face sanctions 
at Friday drinks.

More generally, it is often the case that multiple systems are in operation at once.
Consider a social situation where family, friends, and workmates are present. All three 
sets of expectations are in play. This tends to pull us to the centre, to the expectations 
that the systems have in common.

<p align="center">
  <img src="docs/diagrams/rendered/Three%20Contexts.png" alt="Village Link diagram" width="450" />
</p>

This effect can be spun either positively or negatively. the positive spin would be that the layering 
produces a civilising effect, a pull to the political centre. The negative spin might note a chilling
effect: that additional sets of eyes on Alex can encroach on his liberty.

Either way, the effect is conservative. It tends to connect actions to accountability. This is a
counterbalance to the opposite effect in a 'clickbait' information ecology where actions are 
deliberately isolated from accountability.

## Links

The project introduces an odd-looking URI. The URI is an identifier of an edge in this graph. It is built from three pieces:
1. A marker that this URI is a 'village link' and not a conventional hyperlink
2. A complete, well-formed URI for the first entity
3. A complete, well-formed URI for the second entity.

With this object in hand, the assertion:

> Entity A in system X ...... _equals_ ...... entity B in system Y

Becomes a single, two-ended hyperlink:

> https://village.link/link/{left-uri}//{right-uri}
> 
> (Note there's nothing special about the domain name, 'village.link' in this example. _Any_ domain can make
> assertions of this type.)

This object _can_ resolve to a page that contains additional information about the edge, but it does
not have to do this. It connects three parties, all of which are identified by the URI in a self-contained 
way:

1. The publisher of the link is identified by the web page on which it appears
2. The _left-uri_ identifies the entities inside the first governance system
3. The publisher is asserting that this is the _same_ entity as in the _right-uri_ ... but inside a different governance system. 

The following URI is making an assertion about Joe Rasmussen, the author of this paper:

> https://village.link/link/facebook.com/joerasmussen.70//github.com/Joe-Rasmussen

## Global Context

The project has to be able to connect offline systems like 'my workplace' with online
systems like 'Facebook'. To achive this, we need a few additional lablelling conventions
that belong properly in the specifications document. One of these is important enough to be
mentioned here:

We need a way to assert global context. That is to say, sometimes we want to make assertions 
about 'the real' Joe Rasmussen - the physical presence in the world one that can make an
appearance in _any_ of the other governance systems. This is achieved by adding a prefix 'gc'
to the beginning of a URI.

> <u>gc.village.link/JoeRasmussen</u>
>
>(Note that there is no central authority in this system - nothing special about the 'village.link' domain. 
> _Any_ domain can make a global context assertion of this type.)

## Star Credential

A collection of links like this can be used to establish a 'star credential

<p align="center">
  <img src="docs/diagrams/rendered/Multiple%20Memberships%20Joe%20v2.png" alt="Multiple memberships — Joe, version 2" width="450" />
</p>


The centrepoint of this diagram, with its spokes, establishes a
credential, *🞷JoeRasmussen*. We don’t need any specific technology to
manage this credential - the technologies are managed out in the spokes,
by the different memory systems.

The credential, *🞷JoeRasmussen*, is a collection of as many
*@JoeRasmussens* as he wishes to add.

### An Example

The screen-shot below does not belong to the project, but is useful[^1]:

<p align="center">
  <img src="docs/diagrams/rendered/Steve%20Bynes%20homepage.png" alt="Steve Byrnes homepage" width="650" />
</p>

Byrnes is making a series of claims of fact. The project will make this
same set of claims, but in a standardised way. We need to crawl the web,
and make billions of statements of this type:

- Steve Byrnes is *this entity* on GitHub

- Steve Byrnes is *this entity* on Twitter

- Steve Byrnes is *this person* at UC Berkeley

- Steve Byrnes is an AI Safety researcher

- And so on …

Note the civilising effect of Byrnes’ document: He has an account on
Twitter, and is exposed to Twitter’s technology of memory. That
technology is tuned for the commercial effect of clickbait. It tends to
pull to tribalism, away from the political centre. But Byrnes, by
explicitly linking his reputation in Twitter to his broader set of
memory systems, is less likely to take up Twitter’s invitation to
misbehave.

Byrnes has made it possible for his colleagues in the villages of
academia to link through to his reputation in the Twittersphere. Byrnes’
publication of these links creates a promise that he is prepared to live
by multiple sets of rules at once.

The Village Link project will standardise that promise.

### Authentication

When *🞷JoeRasmussen* and *🞷SteveByrnes* meet, the credentials identify
which technologies they have in common. They can establish two-, three-,
or more-factor authentication through the paths of the web.

<p align="center">
  <img src="docs/diagrams/rendered/Intersection%20of%20Joe%20and%20Steve.png" alt="Intersection of Joe and Steve" width="450" />
</p>

At this point it is easy to lock-on to thinking only about online
technologies. The project seeks wider applicability.

For example, the two credentials, *🞷JoeRasmussen* and *🞷SteveByrnes*,
might reveal that Joe and Steve are family. Families have deep
memory systems, designed originally by evolution as a survival
strategy for a harsh environment.

‘Family’ is a technology that relies on thousands of tiny threads that
wrap back through the collective memory. The ancestral home of family,
the hearthstone, is a thousand-factor authentication system that is
instantaneous, effortless, and infallible. It sets the bar for this type
of technology.

### The Link - Specification

The domain name system, and the URI, are well-suited to the project. The
URI below means ‘Joe Rasmussen in the context of Facebook’:

> [<u>www.facebook.com/joe.rasmussen.70</u>](http://www.facebook.com/joe.rasmussen.70)

We don’t have a URI for: ‘Joe Rasmussen in the global context,’ but the
project owns the domain, <u>village.link</u>, so we can make:

> <u>gc.village.link/JoeRasmussen</u>

(GC - Global Context)

Now we can specify the ‘link’ object that is fundamental to the project:

> Entity A in context X ……………. equals ……….…… entity B in context Y
>
> <u>gc.village.link/JoeRasmussen</u> … equals …
> [<u>www.facebook.com/joe.rasmussen.70</u>](http://www.facebook.com/joe.rasmussen.70)

We don’t want a central authority for this web. There shouldn’t be
anything special about <u>village.link</u>. The URI below would *also*
mean ‘Joe Rasmussen in the global context’, but with the assertion
coming from GitHub, rather than from the Village Link project:

> [<u>gc.github.com/JoeRasmussen</u>](http://gc.github.com/JoeRasmussen)

In the examples above, domain names are contexts - they are memory
systems. We also need a way to label offline memory systems that do
not own a domain - systems like ‘the ancestral home’:

> <u>vc.village.link/AncestralHome</u>
>
> [<u>vc.github.com/AncestralHome</u>](http://vc.github.com/GradmasChristmas)

(VC - Village Context)

### Generality

At this point, the URI has gifted the project with a significant
level-up in generality. A URI can label not just people and contexts,
but *any object*.

> <u>a.context.for/a/label/for/[any/kind/of](http://any.kind.of)/object</u>

This means we can fold any type of object into our web of memory
systems. Most obviously we are interested in the reputational traces of
companies, governing bodies, and other types of organisation … but also
servers, databases, applications … goods and services … and, critically,
AI Agents.

A memory system is a set of constraints, of rules. It might be as
formal as written law, or as informal as the understandings of a group
of friends who meet for Friday drinks.

We care about the constraints on AI, both from a training perspective,
where there is an existing literature about RLHF (reinforcement learning
with human feedback); and also as a contribution to the discussion about
AI alignment.

### AI Alignment

We want AIs to face constraints that are similar to the ancient
constraints faced by humans. To achieve this, we need AI to have
reputational ‘skin in the game’. That is to say, we want AIs that are
subject to the evolving sets of rules that we are calling memory
systems. We need them to experience risk in the face of the sanctions
that are available to those systems.

What could ‘risk’ mean for an AI?

In a population of AIs, some will be relatively effective at
participating in transactions that add value, and others less so. The
AIs that are not adding value will face selection pressure. This is
already true. Frontier AIs are attracting huge resources. The AIs of two
years ago are not.

But it’s not really the AI that is the unit of selection. Good *ideas*
that contribute to effective AIs will tend to be passed down into
subsequent releases, where weaker ideas will tend to go extinct. The
unit of selection is the meme. AI memes, like all units of heredity, are
competing for energy and media.

‘Risk,’ for an AI design meme, means the danger of being cut off from
either energy or media.

### Fraud Prevention. Defence

The Village Link project is building a world where the best defence
against fraud is a ‘star’ credential of the type *🞷HelpfulAI*.

If *🞷HelpfulAI* is proposing a transaction with *🞷SteveByrnes,* Steve is
going to apply his normal firewall. That means finding memory
systems that Steve trusts, and where *🞷HelpfulAI* has left a memory
trail of transactions that demonstrate added value.

The other parties to those transactions are the referees of
*🞷HelpfulAI*. If the AI has no referees, and no reputational skin in the
game, Steve will not engage … and if *no-one* engages, eventually the AI
will be starved of energy. The weaker memes that caused it to fail to
add value in transactions will go extinct.

In a world where the extraction of energy is a collaboration, the
collaborators, individually, have incentive to take as much as they can
for themselves. Collectively, they have incentive to create rules that
punish cheating. The push and shove between these competing goals drives
endless change in systems of rules.

The project folds AIs into the alignment mechanism that is already in
place for our own species. Our great evolutionary trick is to make
transactional systems - villages - that can:

1.  Develop technologies to extract energy from any environment

2.  Solve the problem of distributing the energy among the villagers

3.  Defend the energy store against raiders, internal or external.

### The Reputation of Publishers

The largest of the start-up tasks for this project is to crawl the web
and make some number of billions of statements of the form:

1.  The real Joe Rasmussen … equals …
    [<u>www.facebook.com/joe.rasmussen.70</u>](http://www.facebook.com/joe.rasmussen.70)

This set of statements, published by Village Link, will establish the
web of memory systems. It will give its users the new ‘star’
credential and make it easy to search for multiple authentication paths
between entities. It will be useful on day one.

But the force of a claim published by Village Link is not the same as
the force of a ‘first person’ claim made by an entity, even when the two
claims assert the same fact. Below is ‘the real’ Joe Rasmussen
publishing the same claim as in statement (1) above:

2.  *I am* ……………. equal to …………….
    [<u>www.facebook.com/joe.rasmussen.70</u>](http://www.facebook.com/joe.rasmussen.70)

The system is symmetrical, so we can have the same claim again in the
opposite direction, published from the Facebook account:

3.  [<u>www.facebook.com/joe.rasmussen.70</u>](http://www.facebook.com/joe.rasmussen.70)
    …… is equal to …… the real Joe Rasmussen

Note the symmetry properties of the three statements. In statements (2)
and (3) there is a ‘first person’ that is making a claim about itself.
In contrast, the statement of type (1) is coming from a third party.

In statements (2) and (3), the village links are nearly identical to
hyperlinks. They are directional edges in a node-and-edge graph with an
arrow at one end. They point from one place to another. The source of
the arrow is the publisher of the information.

But the link in statement (1) is different. It is superficially like a
hyperlink, but it has arrows on both ends. It has a publisher that is
different from the entities at either end. The publisher is a third
party in the data structure.

The differences of symmetry have implications for *search*, and suggest
modifications to the existing algorithms that are designed for that
task.

### Search

The key insight, from Larry Page in 1997, is that The Web is a
memory system that encodes reputation. Inside that system, hyperlinks are votes. The diagram
below is taken from the Wikipedia entry for the PageRank search
algorithm:

<p align="center">
  <img src="docs/diagrams/rendered/Wikipedia%20-%20PageRank.png" alt="Wikipedia PageRank diagram" width="550" />
</p>

In the diagram, the circles are web pages and the arrows are hyperlinks.
The percentages, and the size of the circles, show how the algorithm
will rank each page. Page E has six votes, (six inbound hyperlinks,) but
it ranks lower than Page C, which has only one vote.

This is because five of Page E’s six votes come from pages with zero
votes in the network. They have been given a minimum weighting. Page C
has just a single vote, but that vote comes from the page with the
greatest weight.

In our Web of Reputation Systems, the same insights apply, but the
symmetry is different. The insights are:

1.  The edges of the graph are votes

2.  The nodes of the graph have variable weight

3.  The weights are a reflection of reputation in the graph.

To compare village links with hyperlinks we can zoom in and adapt the
PageRank diagram:

<p align="center">
  <img src="docs/diagrams/rendered/PageRank%20Diagram%20adapted.png" alt="Adapted PageRank diagram" width="550" />
</p>

1.  Some entities (yellow) assert that they have global context, “I am
    the real Joe Rasmussen”

2.  Entities can construct a composite credential, *🞷JoeRasmussen*, with
    arrows that face outwards to different memory systems: In the
    diagram this is given by arrows from yellow to red, green, and
    purple

3.  By symmetry, the system supports the reciprocal assertion “This
    account is owned by the real Joe Rasmussen”: In the diagram this is
    the arrow from green back to yellow

4.  Third parties (orange) can use *a pair* of hyperlinks to make a
    double-headed arrow that asserts the equivalence between two
    entities in different contexts:

> Entity A in context X (yellow) … equals … entity B in context Y
> (green).

### Next Steps

The project is at a point where it needs resources - a build team and a
critical path. Some parts of the project are clearly ‘infrastructure,’
and have a natural custodian that is a not-for-profit organisation,
perhaps similar to the IETF, W3C, or the Linux Foundation.

But the project aims to shake up the web, so there are also commercial
opportunities.

The remaining sections consider which parts of the project naturally
belong to shared infrastructure, and which support commercial products.

### Identity, Authentication, Credentials

Clearly this topic is ‘infrastructure’. It is so lightweight that the
‘star’ credential almost exists as soon as it is named. All the heavy
authentication lifting is done by the existing technologies that are
located in the spokes of the star. Steve Byrnes has already built this
credential. He is lacking only a standardised way of publishing it.

The main task for the infrastructure part of the project is to make this
standard, and then launch it with sufficient force that it has a chance
of establishing itself. The strategy for generating this force is
twofold:

1.  Create billions of instances of the ‘link’ object from sources in
    the public domain

2.  Use some degree of ‘shock value’ at launch, when an already-existing
    public data source is consolidated into something that is more
    accessible … and more explicitly linked to reputation. From a
    marketing perspective, this is specifically *your* reputation … so
    you had perhaps best take a look, and maybe clear a few things up by
    making some claims of your own.

### Browser

One option is to treat the browser as infrastructure.

The not-for-profit precedent is Mozilla. There is an argument for
treating the browser as infrastructure, and heading down the bumpy track
created by Mozilla and Firefox. This could be a third leg of the ‘launch’
strategy - that there is a new browser that ‘understands’ that village
links are a special case of hyperlinks. This browser would be optimised
to look for and deal with the special objects, including:

- Entities that claim global context

- Star credentials

- Labels for contexts that do not own a domain (like ‘AncestralHome’)

- *Pairs* of hyperlinks that claim equivalence between entities in
  different contexts.

An alternative, and more ambitious approach, would be to create a
commercial project that packages-up *browser* together with *search*,
*firewall*, and *marketplace*, and attempts to disrupt the incumbents in
these spaces. These incumbents are quite well-resourced![^2] It might be
a ride.

### Search

This will be a fun development project. All the key insights are known,
and there is an existing, open-source literature on optimizing search
for node-and-edge graphs. The novelty, the opportunity, comes from the
new symmetries of the new objects.

Project: Known path to a novel, but consequential outcome. Fun.

### Firewall

For the Village Link project, *Search* and *Firewall* are two faces of
one object. *Search* is the positive, opportunity-seeking side of the
equation. *Firewall* is all those opportunities not pursued, because
they did not clear the bar of trust. Those opportunities failed on risk,
on transaction cost.

### Marketplace

In one sense, *Marketplace* is revealed as yet another facet of the same
set of functions.

*Search* is finding the opportunity. It navigates the Web of Reputation
Systems to find the right provider at the right price for the current
opportunity.

*Firewall* is controlling transaction costs by sidelining the provider
who would like to take your money, (or perhaps your other resources -
sex, media, energy,) but cannot produce the referees, or is not
operating in a known legal framework, or cannot demonstrate reputational
skin in the game.

### Marketplace: Reputation

*Marketplace* is also the right place to summarise two key points from
earlier in the paper:

#### One

In the first description of how we would make a link from one memory
system to another, the paper drew attention to *people* as the common
link. This statement was a useful first approximation, but it was not
general enough.

The project uses the URI to wrap a set of memory systems around *any
object*. This can include a company, or any product or service. It can
include AI Agents, especially if we form the habit of insisting that
they approach us with a credential.

#### Two

Identity, authentication, and credentials were used as the ‘way in’ for
this paper. But the reputational claim, “I am me,” is the least
ambitious of the claims we might make.

The questions below are about the reputations of *people* and *other
things*. Only the first question is about identity. The last question is
a self-referential one about the reputation of a memory system.

Are you who you say you are? … Where are my customers? Who will fund me?
Who will employ me? What is the best product for my current need? What
is the best code snippet to patch this bug? What will the judge think if
I make this argument? What is my best investment opportunity? Is this
idea patentable? Who is most likely as a good romantic partner? What
liquid is that company pumping into my river? What skills should I be
practicing? What can I eat? What chair would look good in the living
room? What is the right AI Agent for me? … What sets of rules apply in
this situation?

### Linked Villages

In the title of this project, the word ‘village’ comes with positive and
negative associations. It is useful to convey a sense of community, of
the personal warmth of belonging. It’s also helpful to have a word that
hearkens to a pre-state reality, and connects to a sense that the
village is an *evolved* response to the challenge of survival.

But pre-state villages could be rather thuggish affairs.

That thuggishness survives in the politics of rusted-on support. For the
leader of an organisation who came to power under one set of rules, it
is attractive to lock onto those rules to the exclusion of any others.
No complexity, please. No divided loyalties. Good simple rituals,
symbols, and regalia. Orthodoxy and suppression, huzzah!

But then you tend to get a fortification at the boundary of the village,
and a terrible problem negotiating with the next village over.

Sometimes, villages are awful. This project is about links.

[^1]: I asked for, and got, Byrnes’ permission to use this image in the
    GitHub repo for the project. Fair to say I have now used it far
    beyond the permission I sought. If this paper gets any wider
    distribution I’ll have to ask again.

[^2]: I am writing this paper in Google Docs. I find myself thinking,
    “If I were Google, would I set an AI onto the task of scanning all
    Google docs for commercial threats to the business?”  
    Maybe.  
    What I really need is a tool to work out which word processors I can
    trust.
