<p align="right">
  <img
    src="https://raw.githubusercontent.com/Inky-Tech-Pty-Ltd/VillageLink/main/docs/assets/Village%20Link%20Heritage%20Bridge%20Logo.png"
    alt="VL logo"
    width="130"
  />
</p>

# Village links

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
> The idea of Joe, the meme, in the recollections of his sister, Brigid

But also:

M=Rover

> Rover in the family home  
> Rover at the vet  
> Rover, the source of all those traces up and down Cooper Street  
> The idea of Rover in the recollections of Spot.

A collection of village links of the type above is called a *star credential*: `🞵JoeRasmussen`, `🞵Rover`.

When an entity presents a star credential, it is saying:

> These are the technologies that store my history and reputation. 
> These are the places you can find referees. My behaviour is tested against the norms of these communities, these legal systems. 
> In any proposed interaction with you, these are the frameworks that are available to control transaction cost and risk.
> Will you open your door?

### Governance

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace

The project is testing the claim in the hope of saying something useful about the governance of AI.

# Artefacts

### Draft artefacts in this repo:

- A [codec](prototype/villagelink/codec.py) for the primitive: `vl:<percent-encoded-P>!<percent-encoded-Q>`, where P and Q are the URIs of the two traces
- A [composer](prototype/villagelink/composer.py) of village links and star credentials
- A [utility kit](prototype/UTILITY.md) for developers
- Two test publishers of village links. The rationale is [here](testbed/README.md). One publisher is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a 'raw' [publication page](https://wab.inky.tech/) with no additional editing furniture
- A [browser](prototype/villagelink/browser.py).

### Experiments that have been spun off elsewhere:

- A repo, [Cobble](https://github.com/Inky-Tech-Pty-Ltd/Cobble), where village links are used to cobble-together a memory graph between memes in the records created by an AI chatbot and its conversational partner. 
Does this graph create a coherent, persistent entity that has a reputational asset, and can be held to account?
- A repo, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), motivated by the following provocation and claim-to-be-tested:
    > **Provocation:** Life is a set of competing 'copy' instructions. Genes are copy instructions expressed in nucleic acids. Memes are copy instructions expressed in _any medium_.  
    > **Claim:** A gene is a special case of a meme.

### Planned artefacts:

- A test graph of many publishers of village links, with publisher reputation an emergent property of the graph
- A Trust Engine: Opportunity/threat. Marketplace/firewall.

