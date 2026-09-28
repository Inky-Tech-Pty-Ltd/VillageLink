# Village links

A village link connects two places where an entity has left a trace in a memory system, say:

> _drosophila_ in Wikipedia <------> _drosophila_ in Britannica

Superficially, a village link resembles a hyperlink, but:

1. A hyperlink points from one place to another. It is a one-headed arrow. A village link is a two-headed arrow. It can be published by a third party
2. A village link asserts *equality*. The thing that is equal is the *idea* behind the traces in the two systems, for example, the idea: 'drosophila'. We are calling this thing, this idea, a *meme*

### Primitive

```text
vl:[A in X]=[B in Y]
```

The traces A and B, in the memory systems X and Y, have the same referent, M. 

```text
M = [A in X]
```

### Star credentials

A village link is agnostic about the technology of memory, so we have:

M=Joe

> Joe-Rasmussen in GitHub  
> joe.rasmussen.70 in Facebook  
> Joseph Rasmussen in the Australian legal system  
> Joe at Friday Drinks  
> Joe in the recollections of his sister, Brigid.

But also:

M=Rover

> Rover in the family home  
> Rover at the vet  
> Rover, the source of all those traces up and down Cooper Street  
> Rover in the recollections of Spot.

A collection of village links of the type above is called a *star credential*: `🞵JoeRasmussen`

### Governance

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace

The project does this in the hope of saying something useful about the governance of AI.

# Information is life

A sister-project, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), is testing a related claim, motivated by the following provocation:

*Life is a set of competing 'copy' instructions. Genes are copy instructions encoded in DNA. Memes are copy instructions encoded in **any medium**.*

> **Claim:** A gene is a special case of a meme.

That project rests on the existing body of work about the way that a meme is governed in a feedback loop with a fitness landscape.

# Artefacts

Existing, in draft:

- A codec for the primitive: `vl:<percent-encoded-P>!<percent-encoded-Q>`, where P and Q are URI identifiers of the two traces
- A composer of village links and star credentials
- Two test publishers of village links. One is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a 'raw' [publication page](https://wab.inky.tech/) with no additional editing furniture
- A browser.

Planned:

- A developer utility kit
- A test graph of many publishers, with publisher reputation an emergent property of the graph
- A trust engine
- An experiment where village links are used to make a memory graph between memes in the records created by an AI chatbot and its conversational partners. Does this create a discrete, persistent entity that has a reputational asset, and can be held to account? Can it learn in the wild?

