# Village links

A village link asserts equality between two expressions of a meme:

> _drosophila_ in Wikipedia <-----> _drosophila_ in Britannica

This does not mean the animal, _Drosophila melanogaster_. It does not mean the Wikipedia entry, and it does not mean the Britannica entry. It means the _idea_ of drosophila, the _meme_.

A village link has a superficial resemblance to a hyperlink, but:

* A hyperlink points from one place to another. It is a one-headed arrow. A village link is a two-headed arrow
* A village link asserts equality.

### Primitive

```text
vl:[A in X]=[B in Y]
```

In other words, the traces A and B, in the memory systems X and Y, have the same referent, a meme, M. 

```text
M = [A in X] = [B in Y]
```
In other words, and more carefully, the trace-in-the-memory-system _is_ the meme.

### Star credentials

A village link is agnostic about technology; about the medium that expresses the meme, so we have:

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
> The idea of Rover in the recollections of Spot; perhaps especially while Spot is walking down Cooper Street.

A collection of village links of the type above is called a *star credential*: `🞵JoeRasmussen`

### Governance

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a trace

The project does this in the hope of saying something useful about the governance of AI.

# Information is life

A sister-project, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), is testing a related claim, motivated by the following provocation:

*Life is a set of competing 'copy' instructions. Genes are copy instructions expressed in DNA. Memes are copy instructions expressed in **any medium**.*

> **Claim:** A gene is a special case of a meme.

That project rests on the existing body of work about the way a meme is governed in a feedback loop with a fitness landscape. 
If we use the word 'governance' we would usually think of the fitness landscape as _the rules_ - the constraints, institutions and norms - but the concept affords a broader interpretation.

# Artefacts

Existing artefacts in this repo (in draft):

- A codec for the primitive: `vl:<percent-encoded-P>!<percent-encoded-Q>`, where P and Q are URI identifiers of the two traces
- A composer of village links and star credentials
- A developer utility kit
- Two test publishers of village links. One is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a 'raw' [publication page](https://wab.inky.tech/) with no additional editing furniture
- A browser.

Planned:

- A test graph of many publishers, with publisher reputation an emergent property of the graph
- A Trust Engine: Opportunity/threat. Marketplace/firewall
- A model of AI governance.

