#adjusted from: https://github.com/datitran/raccoon_dataset
import os
import glob
import xml.etree.ElementTree as ET

def label_map(path):
  classes_names = []

  for xml_file in glob.glob(path + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
      classes_names.append(member[0].text)
     
  classes_names = list(set(classes_names))
  classes_names.sort()
  
  return classes_names

for label_path in ['train', 'test']:
    classes = label_map(label_path)

label_map_path = os.path.join("label_map.pbtxt")
pbtxt_content = ""

for i, class_name in enumerate(classes):
    pbtxt_content = (
        pbtxt_content
        + "item {{\n    id: {0}\n    name: '{1}'\n}}\n\n".format(i + 1, class_name)
    )
pbtxt_content = pbtxt_content.strip()
with open(label_map_path, "w") as f:
    f.write(pbtxt_content)
    print('Successfully created label_map.pbtxt ')  
