# Village links

A village link connects two places where an entity has left a mark on a memory system, say:

> _drosophila_ in Wikipedia <------> _drosophila_ in Britannica

Superficially, a village link resembles a hyperlink, but:

- A hyperlink points from one place to another. It is a one-headed arrow. A village link is a two-headed arrow. It can be published by a third party
- A village link asserts *equality*. The thing that is equal is the *idea* behind the marks in the two systems, for example, the idea: 'drosophila'. We are calling this thing, this idea, a *meme*

### Primitive

```text
vl:[A]in[X]=[B]in[Y]
```

The marks A and B, in the memory systems X and Y, have the same referent, M.

A village link is agnostic about technology, so we have:

M=Joe

> Joe-Rasmussen in GitHub  
> joe.rasmussen.70 in Facebook  
> Joseph Rasmussen in the Australian legal system  
> Joe at Friday Drinks.

But also:

M=Rover

> Rover in the family home  
> Rover at the vet  
> Rover, the source of all those marks up and down Cooper Street.

A collection of village links of the type above is called a *star credential*.

The project is testing a claim:

> **Claim:** For an entity, governance is neither more nor less than the consequences that arise from the memory systems in which it has left a mark

It does so in the hope of saying something useful about the governance of AI.

# Information is life

A sister-project, [information-is-life](https://github.com/Inky-Tech-Pty-Ltd/information-is-life), is testing a related claim, motivated by the following provocation:

*Life is a set of competing 'copy' instructions. Genes are copy instructions encoded in DNA. Memes are copy instructions encoded in **any medium**.*

> **Claim:** A gene is a special case of a meme.

That project rests on the existing body of work about the way that memes are governed in a feedback loop with fitness landscapes.

# Artefacts

Existing, in draft:

- A codec for the primitive, `vl:[A]in[X]=[B]in[Y]`
- A composer of village links and star credentials
- Two test publishers of village links. One is a [MediaWiki](https://village.link/wiki/index.php/Main_Page). The other is a 'raw' [publication page](https://wab.inky.tech/) with no additional editing furniture
- A browser.

Planned:

- A developer utility kit
- A star credential manager
- A trust engine
- An experiment where village links are used to make a memory graph between memes in the records created by an AI chatbot and its conversational partners.

