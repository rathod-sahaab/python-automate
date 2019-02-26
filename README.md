# python-automate
The python-scripts I used to ease my work. The current projects use SVGS(scalable vector graphics) due to their all text structure and small size are easy to work with.
The scripts generally replace a placeholder text with legit text. Also they rename the file and call system command of **inkscape** to export the file in png format.
command used is
`
    inkscape -z file.svg -e file.png
`
inkscape is a svg editor and creator is great for creating abstact images ang illustration is on par with industry standard applictions as Adobe Illustrator go check it out at [Inkscape's Website](https://inkscape.org)
`-z` suppresses GUI of inkscape
`-e` specifies the output file

## Certies
A certificate template is made **finalcerti.svg** and first text is replaced and the renamed then saved and then is **exported.**

Posts and names were seperated by dashes `-` and different names by new line

## Winter Face-off
Template(wfot.svg) is renamed and replaced for all name pairs in file(names) and then after editing are exported.

space seperated pair of names as only forst names were considered and different pairs by newlines.