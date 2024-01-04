import argparse
import xml.etree.ElementTree as ElementTree

def parse(input,output,packname,add_comments):
	public_tree=ElementTree.parse(input)
	resources=public_tree.getroot()
	dick={}
	for pub in resources.findall("public"):
		type=pub.get("type")
		name=pub.get("name")
		id=pub.get("id")
		if not type in dick:dick[type]=list()
		dick[type].append((name,id))
	with open(output,"w",encoding="utf-8") as rclass:
		rclass.write(f"package { packname };\n\n")
		rclass.write("final public class R\n{\n")
		for type in dick:
			rclass.write(f"\tstatic public class { type }\n\t{{\n")
			for name,id in dick[type]:
				rclass.write(f"\t\tstatic public final int { name.replace('.',"_") }={ id };")
				if add_comments:rclass.write(f"//{ int(id,16) }")
				rclass.write("\n")
			rclass.write("\t}\n\n")
		rclass.write("}")

def main():
	parser=argparse.ArgumentParser(description="Android R class generator based on public resources from decompiled APK with ApkTool")
	parser.add_argument("-i","--input",help="Input public.xml file")
	parser.add_argument("-o","--output",help="Output R.java class file")
	parser.add_argument("-p","--packname",help="Output package name")
	parser.add_argument("-c","--comments",action="store_true",help="Add comments with decimal resource ids")
	args=parser.parse_args()
	if not args.input:
		print("null input file")
		exit(-1)
	if not args.output:
		print("null output file")
		exit(-1)
	if not args.packname:
		print("null packname")
		exit(-1)
	parse(args.input,args.output,args.packname,args.comments)

if __name__=="__main__":main()