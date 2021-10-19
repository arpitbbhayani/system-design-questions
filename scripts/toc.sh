for f in *.md
do
  gh-md-toc --no-backup --hide-footer $f
done
