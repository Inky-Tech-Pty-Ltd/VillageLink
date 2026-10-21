<p align="right">
  <img
    src="https://raw.githubusercontent.com/Inky-Tech-Pty-Ltd/VillageLink/main/docs/assets/Village%20Link%20Heritage%20Bridge%20Logo.png"
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

### Village links
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
In Cobble, the hypothesis may be a candidate memory. In authentication, an entity might present 
the hypothesis _Joe Rasmussen_ to a gatekeeper, such as Hugging Face, as the centrepiece of a star credential. 
The gatekeeper assesses the evidence and decides whether to open the door. 

### Governance

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace

We are testing the claim in the hope of saying something useful about the governance of AI.

## Artefacts

### Draft artefacts in this repo:

- [A codec](prototype/villagelink/codec.py) for the primitive: `vl:<percent-encoded-P>!<percent-encoded-Q>`, where P and Q are the URIs of the two traces
- [A composer](prototype/villagelink/composer.py) of village links and star credentials
- [A utility kit](prototype/UTILITY.md) for developers
- Two test publishers of village links. The approach to publication has its own [README](testbed/README.md). The two publishers are exposed online. One is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a [minimal publication page](https://wab.inky.tech/) with no additional editing furniture
- [A browser](prototype/villagelink/browser.py).

### Experiments that have been spun off elsewhere:

- A repo, [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble), where village links are used to cobble together a memory graph between memes in the records created by an AI chatbot and its conversational partner. 
Does this graph create a coherent, persistent entity that has a reputational asset, and can be held to account?
- A repo, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), motivated as follows:
  
    > **Provocation:** Life is a set of competing 'copy' instructions. Genes are copy instructions expressed in nucleic acids. Memes are copy instructions expressed in _any medium_.  
    > **Claim:** A gene is a special case of a meme.

### Planned artefacts:

- A test graph of many publishers of village links, with publisher reputation an emergent property of the graph
- A Trust Engine that introduces a marketplace of opportunities defended by a firewall of trust.

### Value proposition

#### 1. Authentication

A multi-factor authentication system that is technology-agnostic, and indeed can recruit _any_ existing or future technology.
The project is aiming to deliver a gold standard 'family Christmas' authentication.
'Family Christmas' is authentication _in the graph_ with thousands of tiny factors acting in concert.
It should have the breeziness and sense of infallibility of greeting Uncle John at the door. 

For contrast and conceptual testing, we are using the [July 2026 Hugging Face attack](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

#### 2. A self-sovereign AI entity

An AI entity that is instantiated in a body of work rather than in a suppler of intelligence
* At its centre is a graph of memories connected by Village Links, preserving context across interactions and changes of supplier
* The entity is self-sovereign: as independent as possible of the risks associated with particular suppliers
* The entity is interoperable and portable. It can recruit intelligence from competing suppliers and move between hosting environments without surrendering its accumulated memory and identity
  
#### 3. A Trust Engine

The analogy here is not a search engine spanning the whole web, but the membrane of an organism exposed to opportunities and risks in its environment.
   
Inside the membrane is a coherent entity, connected by Village Links. Outside is the world. 
The problem is to decide where to extend the internal graph to maximise opportunities and minimise risks.
   
```
Trust Engine = f(internal graph, external graph, problem vector)
```
 
The graphs provide the context. The user supplies the problem vector: the opportunity, transaction or question to be assessed.

The ideal interface is an existing search-engine or chatbot query box, requiring no change in the user's habits. The Trust Engine could be delivered as a plugin to those interfaces.
   
(Note that the project also has _governance_ outcomes. These are more properly _public goods_ rather than _value propositions_ for an individual.)

#### 4. Governance

The coherent entity described in (2) above faces opportunities and risks described in (3) above.
The entity may be human or non-human. In either case, the entity makes its way in the world through a set of transactions.
At each transaction proposed by our entity, the other party faces risk. It is in the interest of our entity to present evidence
that will minimise that risk. One way to do this is with the authentication system described in (1) above.
What that authentication system does is to present traces of the entity from a range of memory systems.
The entity is hoping to minimise transaction costs for its potential trading partner by demonstrating that it is 
subject to the norms of those memory systems.

This is the source of the core 'governance' claim of the project:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace.
