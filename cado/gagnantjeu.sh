convert -background  lightblue -fill blue  -pointsize 26 -size 160x140 \
  caption:"$4 a gagné un $5" \
       "./uploads/$6"
convert -page +0+0 "./uploads/$6" -page +160+100 "./uploads/$2" -page +500+100 "./uploads/$1" -background lightblue -layers merge +repage "./uploads/$3"
