#!/bin/sh
set -e
svn=svn://svn.code.sf.net/p/ctags/code
tag=ctags-5.8
out=branch.diff

d=$-
filter() {
	set -$d
	# Excluding files which change version or were not in dist tarball
	filterdiff \
		-x 'NEWS' \
		-x 'maintainer.mak' \
		-x 'Test/*' \
		-x 'website/*' \
		| \
	# remove revno's for smaller diffs
	sed -e 's,^\([-+]\{3\} .*\)\t(revision [0-9]\+)$,\1,'
}

old=$svn/tags/$tag
new=$svn/trunk
echo >&2 "Running diff: $old -> $new"
LC_ALL=C svn diff --old=$old --new=$new > $out.tmp
revno=$(sed -ne 's,^[-+]\{3\} .*\t(revision \([0-9]\+\))$,\1,p' $out.tmp | sort -urn | head -n1)
echo >&2 "Revision $revno"
[ "$revno" -gt 0 ] || exit 1

sed -i -e "1i# Revision $revno" $out.tmp
filter < $out.tmp > $out.tmp2 && mv -f $out.{tmp2,tmp}

if cmp -s branch.diff{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f branch.diff.tmp
	exit 0
fi
mv -f branch.diff{.tmp,}
