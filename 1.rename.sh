#script to rename file names that contain blank spaces and special characters " " and replace them with "-" char
#paste the script in every location your files are and run it from its directory
#if you are on Win OS, install cygwin and after successful installation run the script on Win cmd
#!/bin/bash
invalid="[^a-zA-Z_0-9.-]" #regex, ^ inside - negates the character class
FILES=*
for f in $FILES
do
  echo "Processing $f file..."
  if [[ $f == *$invalid* ]]; then
	newname=$(echo $f | sed 's/[^a-zA-Z_0-9.-]/-/g')
    mv "$f" $newname
  fi
done
