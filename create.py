from world_generator.world import ( Tree, World, Field)



world = World()

ground_level = Field(world=world)
tree = Tree(x=10, y=10, world=world)