# the plan:

produe a useful tool for managing a stage at a live event.

provide SM with instant access to communications and information for the relelvant acts, crew, etc.

# initial thoughts

## sql vs graph
deeply self referential data.  
eg, a `Person` might be both an `Artist` and a `Crewmember`, they might play
music with multiple `Acts` each `Act` might be playing multiple `Performances` at a single `Event` but at different `Venues`.

effecient access all relationships, eg, all the shows on a given stage, or all the acts in a show.  
would graph be better than sql? why?

