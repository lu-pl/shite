# shite

`shite` is a tiny *macro* language for SHACL that implements conditionals.

The *acronym* `shite` stands for **SH**acle **I**f **T**hen **E**lse. If you read it as an *apronym*, that's on you. 🤭

### Concept

`shite` defines a meta-shapes graph that is meant to be run against a shapes graph by a SHACL processor. Note that `shite` requires a SHACL processor that supports `sh:SPARQLRule` from [SHACL Advanced Features](https://www.w3.org/TR/shacl-af/#rules).

The general  idea of `shite` is to introduce a vocabulary for `if-then-else` that macro-transforms to the respective `and-or-not` expressions.

`shite` defines

1. conditional terms `shite:if`, `shite:then` and `shite:else`
2. a grammar for if-then-else enforced by SHACL shapes
3. macro-expander shapes that transform `shite` terms into `sh:and`/`sh:or`/`sh:not` constructs

The following SHACL shapes graph uses `shite` terms to define conditional constraints such that, if the target node has `<urn:x>` asserted about it, it must also have `<urn:y>` asserted about it; else, it must have `<urn:z>` asserted about it.

```turtle
@prefix ex: <http://example.org#> .
@prefix shite: <https://github.com/lu-pl/shite#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:Shape a sh:NodeShape ;
	sh:targetNode <urn:target> ;
	shite:if [
		sh:property [
			sh:path <urn:x> ;
			sh:minCount 1 ;
			sh:maxCount 1
			]
		] ;
	shite:then [
		sh:property [
			sh:path <urn:y> ;
			sh:minCount 1 ;
			sh:maxCount 1
			]
		] ;

	shite:else [
		sh:property [
			sh:path <urn:z> ;
			sh:minCount 1 ;
			sh:maxCount 1
			]
		] .

```

Running a SHACL AF processor with `shite` as the *shapes graph* and the above SHACL graph as the *data graph* validates and expands the given `shite` terms and transforms the data graph like so:

```turtle
@prefix ex: <http://example.org#> .
@prefix shite: <https://github.com/lu-pl/shite#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:Shape a sh:NodeShape ;
	sh:targetNode <urn:target> ;
	sh:or (
		[
			sh:not [
				sh:property [
					sh:minCount 1 ;
					sh:maxCount 1 ;
					sh:path <urn:x>
					]
			]
		]
		[
			sh:property [
				sh:minCount 1 ;
				sh:maxCount 1 ;
				sh:path <urn:y>
				]
		]
	),
	(
		[
			sh:property [
				sh:minCount 1 ;
				sh:maxCount 1 ;
				sh:path <urn:x>
			]
		]
		[
			sh:property [
				sh:minCount 1 ;
				sh:maxCount 1 ;
				sh:path <urn:z>
			]
		]
	) .
```

The expanded data graph can then be used as a shapes graph to validate another data graph.

According to the above expansion, the following validates

```turtle
<urn:target> <urn:x> "literal" ;
	<urn:y> "other literal" .
```

```turtle
<urn:target> <urn:z> "yet another literal" .
```

```turtle
<urn:target> <urn:y> "other liteal" ;
	<urn:z> "yet another literal" .
```

while this does not pass validation:

```turtle
<urn:target> <urn:x> "literal" .
```

```turtle
<urn:target> <urn:y> "other literal" .
```

```turtle
<urn:target> <urn:x> "literal" ;
	<urn:z> "yet another literal" .
```
