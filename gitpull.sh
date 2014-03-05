#!/bin/bash
export LANG=C
export LC_MESSAGES=C

if [[ "$(git remote)" != *systemd-rhel7* ]]; then
    git remote add systemd-rhel7 git+ssh://git.engineering.redhat.com/srv/git/users/harald/systemd-rhel7.git
fi

git rm -f [0-9][0-9][0-9][0-9]*.patch

git fetch systemd-rhel7
git format-patch -M -N --no-signature v208..systemd-rhel7/master
for i in [0-9][0-9][0-9][0-9]*.patch; do
	[ -f "$i" ] || continue
	git add "$i"
done

IFS="
"
while read -r line; do
    case "$line" in
        Patch[0-9][0-9][0-9][0-9]*)
            ;;
        *RHEL-specific*)
            printf "%s\n" "$line"
            for i in [0-9][0-9][0-9][0-9]*.patch; do
                printf "Patch%s: %s\n" "${i%%-*}" "$i"
            done
            ;;
        *)
            printf "%s\n" "$line"
            ;;
    esac
done < systemd.spec >systemd.spec.new
mv systemd.spec.new systemd.spec
