convert -background lightblue -fill blue -size 320x140 \
     caption:"$1" \
        "./uploads/$4"

convert -border 10x10 -bordercolor lightblue -page +50+10 "./uploads/$4" -page +100+150 "./uploads/$2" -page +500+100 ./cado/metisfmlogo.png -background lightblue -layers merge +repage "./uploads/$3"
