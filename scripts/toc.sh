for f in *.md
do
  python ./scripts/footer.py $f
  gh-md-toc --no-backup --hide-footer $f
done
