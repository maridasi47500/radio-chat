convert -background  lightblue -fill blue  -pointsize 26 -size 320x140 caption:"$4 a gagné un $5" "./uploads/$6"
convert -page +0+0 "./uploads/$2" -page +150+100 "./uploads/$6" -page +500+100 "./uploads/$1" -background lightblue -layers merge +repage "./uploads/$3"
