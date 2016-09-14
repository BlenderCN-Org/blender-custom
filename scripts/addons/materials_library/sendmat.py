
import bpy, json
class EmptyProps(bpy.types.PropertyGroup):
	pass
bpy.utils.register_class(EmptyProps)
bpy.types.Scene.matlib_categories = bpy.props.CollectionProperty(type=EmptyProps)
cats = []
for cat in bpy.context.scene.matlib_categories:
	materials = []
	for mat in bpy.data.materials:
		if "category" in mat.keys() and mat['category'] == cat.name:
			materials.append(mat.name)
	cats.append([cat.name, materials])
with open("F:\\Work\\blender-custom\\scripts\\addons\\materials_library\\categories.txt", "w") as f: 
	f.write(json.dumps(cats, sort_keys=True, indent=4))
