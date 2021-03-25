#! /bin/bash
OIFS="$IFS"
IFS=$'\n'
export MAGICK_TMPDIR=/run/media/aclef/BT/tmp/
for f in `find . -maxdepth 1 -type f -name "*.pdf"`
do
    echo $f
    pdftk $f dump_data | grep '^Bookmark' > ./bookmarks
    mkdir pics/
    pdfseparate $f pics/output-%05d.pdf
    cd pics/
    #convert -limit thread 1 -limit memory 500MiB  -density 200 $f pics/output-%05d.png
    for page in `find . -maxdepth 1 -type f -name "*.pdf"`
    do
        convert -limit thread 1 -limit memory 500MiB -density 450 $page "${page}.png"
        rm $page
    done
    
    rm *.pdf
    
    #cd pics/
    jbig2 -s -p -v *
    pdf.py output >out.pdf
    cd ..
    mv ./pics/out.pdf ./compressed.pdf
    rm -r pics/
    pdftk ./compressed.pdf update_info ./bookmarks output $f
    rm ./bookmarks
    rm ./compressed.pdf
done
IFS="$OIFS"
