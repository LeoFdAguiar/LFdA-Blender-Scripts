import bpy
import datetime

t = datetime.datetime.now()

## GET TRI EDGES (First Condition)###########################################
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='DESELECT')

## create list to store triangle edges IDs (edges for first condition) 
tri_edge_ids = []

## Select all edges of triangles and store their IDs in list created above
bpy.ops.mesh.select_face_by_sides(number=4, type='LESS', extend=False)

## switch to Object Mode first for the selected edges to get "registered"
bpy.ops.object.mode_set(mode = 'OBJECT')

## store edges in list created above and sort list
for edge in bpy.context.active_object.data.edges:
    if edge.select:
        tri_edge_ids.append(edge.index)

tri_edge_ids.sort()

## Print the list with edge indecies to the console for debugging purposes
print(t, "Tris edge IDs (3 sided faces): ", tri_edge_ids)
############################################################################


## GET NON MANIFOLD EDGES (Second Condition)##################################
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='DESELECT')

## create list to store non-manifold edges IDs (edges for second condition)
non_manifold_edges = []

## Select non-manifold edges and store their IDs in list created above
bpy.ops.mesh.select_non_manifold()

## switch to Object Mode first for the selected edges to get "registered"
bpy.ops.object.mode_set(mode = 'OBJECT')

## store edges in list created above and sort list
for edge in bpy.context.active_object.data.edges:
    if edge.select:
        non_manifold_edges.append(edge.index)

non_manifold_edges.sort()

## Print the non-manifold edge IDs to the Console for debugging purposes        
print(t, "Non-manifold edge IDs: ", non_manifold_edges)
############################################################################

## GET MATCHING EDGES ########################################################
bpy.ops.object.mode_set(mode = 'EDIT')     
bpy.ops.mesh.select_all(action='DESELECT')

## Create list for storing matched edges
## Assign to the list only the edges whose ID is present in both lists 
matching_edges = list(set(tri_edge_ids) & set(non_manifold_edges))        
matching_edges.sort()

## switch to Object Mode first for the selected edges to get "registered"  
bpy.ops.object.mode_set(mode = 'OBJECT')

for edge in matching_edges:
    bpy.context.active_object.data.edges[edge].select = True
            
## Print the matching edge IDs to the Console for debugging purposes        
print(t, "Matching Edge IDs: ", matching_edges)

bpy.ops.object.mode_set(mode = 'EDIT')
############################################################################
