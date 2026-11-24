<p align="right">
  <img
    src="docs/assets/Village%20Link%20Heritage%20Bridge%20Logo%20transparent.png"
    alt="VL logo"
    width="130"
  />
</p>

# Village Link
Village Link is an Inky Tech project.

**Inky Tech Pty Ltd**   
Infrastructure of memory.

_Memory is the masterpiece.  
Intelligence is paint._

## Village links
A village link asserts equality between two expressions of a meme:

> _drosophila_ in Wikipedia <-----> _drosophila_ in Britannica

This does not mean the animal, _Drosophila melanogaster_. It does not mean the Wikipedia entry, and it does not mean the Britannica entry. It means the _idea_ of drosophila, the _meme_.

A village link has a superficial resemblance to a hyperlink, but:

* A hyperlink points from one place to another. It is a one-headed arrow. A village link is two-headed
* A village link asserts equality.

### Primitive

```text
vl:[A in X]=[B in Y]
```

In other words, the traces A and B, in the memory systems X and Y, have the same referent, a meme, M. 

```text
M = [A in X] = [B in Y]
```
Or, more carefully, the trace-in-the-memory-system _is_ the meme.

The equality is strict, but a village link is an assertion made by an entity in context, not an established fact. 
An entity or process may evaluate that assertion as TRUE or FALSE and use the result in Boolean operations.

### Star credentials

A village link is agnostic about technology — about the medium in which the meme is expressed. So we can have:

M=Joe

> Joe-Rasmussen in GitHub  
> joe.rasmussen.70 in Facebook   
> Joseph Rasmussen in the Australian legal system  
> Joe at Friday Drinks  
> Joe's bicycle (which seems a ridiculous meme-carrier until you consider Hadrian's Wall)   
> The idea of Joe in the recollections of his sister, Brigid

But also:

M=Rover

> Rover in the family home  
> Rover at the vet  
> Rover, the source of all those traces up and down Cooper Street  
> The idea of Rover in the recollections of Spot.

A collection of village links of the type above is called a *star credential*: `🞵JoeRasmussen`, `🞵Rover`. 

A star credential asserts a set over which a meme is invariant.

When an entity presents a star credential, it is saying:

> These are the memory systems that store my history and reputation, and demonstrate my skills. These are my technologies of authentication.
> These are the places you can find referees. My behaviour is tested against the norms of these communities. I am subject to these legal systems. 
> In any proposed interaction with you, these are the frameworks that are available to control transaction cost and risk.
> Will you open your door?

From the perspective of the primitive, the centre of a star is a meme like any other. 
In practice, we have found it useful to call this meme the _hypothesis_.
In the sister-project of Village Link, [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble/blob/main/README.md), the hypothesis may be a _room_. 
In an authentication process, an entity might present 
the hypothesis _Joe Rasmussen_ to a gatekeeper, such as Hugging Face, as the centrepiece of a star credential. 
The gatekeeper assesses the evidence and decides whether to open a door. 

## Governance

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace.

We are testing the claim in the hope of saying something useful about the governance of AI.

## Value proposition

### 1. Authentication

The project will deliver a multi-factor authentication system that is technology-agnostic, and indeed can recruit _any_ existing or future technology.
We are aiming for a gold standard of 'family celebration' authentication.
'Family celebration' is authentication _in the graph_ with thousands of tiny factors acting in concert.
It should have the breeziness and sense of infallibility of greeting Uncle John at the door. 

For contrast and conceptual testing, we are using the [July 2026 Hugging Face attack](https://openai.com/index/hugging-face-incident-and-the-road-ahead/).

### 2. A self-sovereign entity (See [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble/))

The project aims to build an entity that is instantiated in a body of work rather than in a supplier of intelligence:
  
### 3. A Trust Engine

The analogy here is not a search engine spanning the whole web, but with the membrane of an organism exposed to opportunities and risks in its environment.
   
Inside the membrane is a coherent entity. Outside is the world. 
The problem is to decide where to admit the possiility of change in the internal state to maximise opportunities and minimise threats.
   
```
Trust Engine = f(internal graph, evidence at the membrane, problem vector)
```

### 4. Governance

_(The three items above are value propositions with benefits that accrue to an individual entity.
This item is more properly understood as a public good, with benefits that accrue to a community, sometimes represented by a governance entity.)_

The Trust Engine described in (3) above is designed to navigate the risks and opportunities faced by an entity.
The entity may be human, or it may be a coherent self-sovereign entity of the type described in (2) above. 

In either case, the entity accesses resources through a series of transactions.
In each transaction, the entity faces another party. The other party experiences risk.

Our entity maximises its opportunity by minimising transaction costs. 
The authentication system described in (1) above is the key asset in this effort.
It says, "Your risk is controlled because I am constrained by the rules and norms of these communities."

This is the source of the core governance claim of the project:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace.

## Artefacts

### Draft artefacts in this repo:

- [A codec](prototype/villagelink/codec.py) for the primitive: `vl:<percent-encoded-P>!<percent-encoded-Q>`, where P and Q are the URIs of the two traces
- [A composer](prototype/villagelink/composer.py) of village links and star credentials
- [A utility kit](prototype/UTILITY.md) for developers
- Two test publishers of village links. The approach to publication has its own [README](testbed/README.md). The two publishers are exposed online. One is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a [minimal publication page](https://wab.inky.tech/) with no additional editing furniture
- [A browser](prototype/villagelink/browser.py).

### Experiments that have been spun off elsewhere:

- A repo, [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble), with a prototype app to cobble together an entity from information sources and intelligence sources. 
Does this functionality create a coherent, persistent entity that has a reputational asset, and can be held to account?
- A repo, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), motivated as follows:
  
    > **Provocation:** Life is a set of competing 'copy' instructions. Genes are copy instructions expressed in nucleic acids. Memes are copy instructions expressed in _any medium_.  
    > **Claim:** A gene is a special case of a meme.

### Planned artefacts:

- A test graph of entities with market incentives and reputational constraints
- A Trust Engine that assesses oppotunities and threats at the membrane of an entity.
