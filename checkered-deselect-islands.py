import bpy
import bmesh

#define function that will deselect every other vert from all verts selected
def checkered_deselect(obj, bm):
    selected_verts = [v for v in bm.verts if v.select]
    for i, vert in enumerate(selected_verts):
        if i % 2 == 1:
            vert.select = False
    bm.select_flush(False)

obj = bpy.context.object
if obj and obj.type == 'MESH':
    bpy.ops.object.mode_set(mode='EDIT')
    bm = bmesh.from_edit_mesh(obj.data)
    checkered_deselect(obj, bm)
    bmesh.update_edit_mesh(obj.data)
else:
    print("Please select a mesh object.")

#space out the verts (requires looptools addon)
bpy.ops.mesh.looptools_space(influence=100, input='selected', interpolation='cubic', lock_x=False, lock_y=False, lock_z=False)
