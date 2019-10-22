from firedrake.petsc import PETSc
from functools import partial

class PardecompOverlap(object):
    @staticmethod
    def select_entity(p, dm=None, exclude=None):
        """Filter entities based on some label.

        :arg p: the entity.
        :arg dm: the DMPlex object to query for labels.
        :arg exclude: The label marking points to exclude."""
        if exclude is None:
            return True
        else:
            # If the exclude label marks this point (the value is not -1),
            # we don't want it.
            return dm.getLabelValue(exclude, p) == -1

    @staticmethod
    def star(dm, p):
        return dm.getTransitiveClosure(p, useCone=False)[0]

    @staticmethod
    def closure(dm, p):
        return dm.getTransitiveClosure(p, useCone=True)[0]

    def __call__(self, pc):
        dm = pc.getDM()
        prefix = pc.getOptionsPrefix()
        opts = PETSc.Options(prefix)

        select = partial(self.select_entity, dm=dm, exclude="pyop2_ghost")
        (pStart, pEnd) = dm.getChart()
        owned_entities = set(filter(select, range(pStart, pEnd)))

        overlap = 1 # FIXME: get from options
        all_entities = set(owned_entities)
        for i in range(overlap):
            tmp_entities = set(all_entities)
            for entity in tmp_entities:
                for s in self.star(dm, entity):
                    for c in self.closure(dm, s):
                        all_entities.add(c)

        overlap_entities = list(all_entities.difference(owned_entities))

        iset = PETSc.IS().createGeneral(overlap_entities, comm=PETSc.COMM_SELF)
        patches = [iset]
        iterset = PETSc.IS().createStride(size=len(patches), first=0, step=1, comm=PETSc.COMM_SELF)

        #print("owned_entities: ", owned_entities)
        #print("all_entities: ", all_entities)
        #print("overlap_entities: ", overlap_entities)
        return (patches, iterset)


