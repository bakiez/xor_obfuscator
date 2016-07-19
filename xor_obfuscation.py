import argparse
import array

def main():
	#argparse values
	parser = argparse.ArgumentParser(description='Password based XOR obfuscator.')
	parser.add_argument("-i","--input_file", help="Input file to be XOR'd", type=str, dest="input_file")
	parser.add_argument("-p","--password", help="Password used to obfuscate input_file", type=str, default="password", dest="password")
	parser.add_argument("-o","--output_file", help="Output file to be written after input_file is XOR'd with password", type=str, default="out.file", dest="output_file")
	parser.add_argument("-v","--verbose", help="Display all information while running", action="store_true")
	args = parser.parse_args()

	#conditions to check before running program
	if args.input_file=="":
		print "No input file, please see -h options."
		quit(1)
	if args.password=="":
		print "No password provided, continuing with default 'password'."
	if args.output_file=="":
		print "No output file specified. Using default.\n"

	#actual main function
	i=0
	password_len = len(args.password)
	if args.verbose:
		print "The length of the password is "+str(password_len)+"\n"
	f = open(args.input_file, "rb")#open input file
	if args.verbose:
		print "The input file has been opened.\n"
	f2 = open(args.output_file, "wb")#open output file
	if args.verbose:
		print "The output file has been opened.\n"
	try:
		j=1
		byte = f.read(1)#read first byte
		if args.verbose:
			print "Bytes are being read...\n"
		while byte != "": #read bytes until there are none left
			pass_byte = args.password[i:i+1]#take one byte from password
			new_byte = chr(ord(byte) ^ ord(pass_byte)) #XOR YAY
			f2.write(new_byte)#write to output file
			if args.verbose:
				print str(j)+" bytes have been written.\n"
			#loop parameter updates			
			i = (i+1) % password_len
			byte = f.read(1)
			j=j+1 #j is used to measure how many bytes have been written
	finally:
		if args.verbose:
			print "Reached finally block."
		f.close()
		f2.close()

if __name__=="__main__":
	main()
			
