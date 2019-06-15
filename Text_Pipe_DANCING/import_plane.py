### OSX

### Models [0 to N]


import bpy



for i in range(106):
# for i in range(30):


    number = "%03d"%(i)
    tmp_name = "obj_" + number

    path = "/Users/iMac-2008/Documents/3D_Morphing_Models_MetaBall/Text_Pipe_DANCING/FBX_Plane/" + number + ".fbx"
    print(path)



    ### Import FBX
    bpy.ops.import_scene.fbx(filepath = path)


    ### get Scene
    scene = bpy.context.selected_objects[0]
    scene.name = "scene"
    scene.scale = (1, 1 ,1)
    scene.rotation_euler = (0,0,0)

    obj = bpy.context.selected_objects[1]
    obj.name = tmp_name
    obj.scale = (1, 2.5 ,1)
    obj.rotation_euler = (0, 0, 0)


    ### Get material
    mat_tmp = bpy.data.materials.get("NormalVec")

    ### Assign it to object
    if obj.data.materials:
        # assign to 1st material slot
        obj.data.materials[0] = mat_tmp
    else:
        # no slots
        obj.data.materials.append(mat_tmp)


    ### Modifier
    bpy.context.scene.objects.active = obj


    ##### SUBSURF
    # bpy.ops.object.modifier_add(type='SUBSURF')
    # bpy.data.objects[tmp_name].modifiers["Subsurf"].render_levels = 2
    #bpy.ops.object.modifier_apply()



    ### KeyFrame Assign
    obj.location = (0, 0, 20)
    obj.keyframe_insert(data_path = "location", frame=i)
    obj.location = (0, 0, 0)
    obj.keyframe_insert(data_path = "location", frame=i+1)
    obj.location = (0, 0, 20)
    obj.keyframe_insert(data_path = "location", frame=i+2)