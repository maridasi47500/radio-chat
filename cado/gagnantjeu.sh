convert -background  lightblue -fill blue  -size 160x140 \
  caption:"$4 a gagné un $5" \
       "./uploads/$6"
convert -border 10x10 -bordercolor lightblue -page +0+0 "./uploads/$6" -page +160+140 "./uploads/$2" -page +500+100 "./uploads/$1" -page +500+100 ./cado/metisfmlogo.png -background lightblue -layers merge +repage "./uploads/$3"
