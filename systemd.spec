# PIE is broken on s390 (#868839, #872148)
%ifnarch s390 s390x
%global _hardened_build 1
%endif

# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
Version:        207
Release:        10%{?dist}
# For a breakdown of the licensing, see README
License:        LGPLv2+ and MIT and GPLv2+
Summary:        A System and Service Manager

Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.xz

# Fedora's default preset policy
Source1:        90-default.preset
Source7:        99-default-disable.preset
Source5:        85-display-manager.preset
# Feodora's SysV convert script. meh.
Source2:        systemd-sysv-convert
# Stop-gap, just to ensure things work fine with rsyslog without having to change the package right-away
Source4:        listen.conf
# Prevent accidental removal of the systemd package
Source6:        yum-protect-systemd.conf
# ship /etc/rc.d/rc.local https://bugzilla.redhat.com/show_bug.cgi?id=968401
Source8:        rc.local


# RHEL-specific:
Patch0001: 0001-RHEL-units-add-Install-section-to-tmp.mount.patch
Patch0002: 0002-kernel-install-add-fedora-specific-callouts-to-new-k.patch
Patch0003: 0003-core-cgroup-first-print-then-free.patch
Patch0004: 0004-swap-fix-reverse-dependencies.patch
Patch0005: 0005-update-TODO.patch
Patch0006: 0006-cryptsetup-generator-don-t-create-tmp-swap-units.patch
Patch0007: 0007-cryptsetup-generator-allow-specifying-options-in-pro.patch
Patch0008: 0008-automount-rename-repeat_unmont-to-repeat_unmount.patch
Patch0009: 0009-cgroup-add-the-missing-setting-of-variable-s-value.patch
Patch0010: 0010-cgroup-correct-the-log-information.patch
Patch0011: 0011-cgroup-fix-incorrectly-setting-memory-cgroup.patch
Patch0012: 0012-random-seed-we-should-return-errno-of-failed-loop_wr.patch
Patch0013: 0013-update-TODO.patch
Patch0014: 0014-libudev-fix-move_later-comparison.patch
Patch0015: 0015-man-document-luks.options-kernel-commandline.patch
Patch0016: 0016-keymap-remove-some-commented-out-lines.patch
Patch0017: 0017-Advertise-hibernation-only-if-there-s-enough-free-sw.patch
Patch0018: 0018-README-add-SCSI-BSG-option.patch
Patch0019: 0019-swap-create-.wants-symlink-to-auto-swap-devices.patch
Patch0020: 0020-cgroup-add-missing-equals-for-BlockIOWeight.patch
Patch0021: 0021-Assume-that-proc-meminfo-can-be-missing.patch
Patch0022: 0022-transaction.c-do-not-point-users-to-logs-when-unit-n.patch
Patch0023: 0023-Verify-validity-of-session-name-when-received-from-o.patch
Patch0024: 0024-udev-rules-avoid-erroring-on-trailing-whitespace.patch
Patch0025: 0025-keymap-Add-Samsung-Series-5-Ultra.patch
Patch0026: 0026-login-fix-login_is_valid-test.patch
Patch0027: 0027-polkit-Avoid-race-condition-in-scraping-proc.patch
Patch0028: 0028-core-whenever-a-new-PID-is-passed-to-us-make-sure-we.patch
Patch0029: 0029-remove-user-.service.patch
Patch0030: 0030-cgroup-always-enable-memory.use_hierarchy-for-all-cg.patch
Patch0031: 0031-logind-return-EINVAL-when-PID-is-wrong.patch
Patch0032: 0032-core-drop-some-out-of-date-references-to-cgroup-sett.patch
Patch0033: 0033-man-explain-NAME-in-systemctl-man-page.patch
Patch0034: 0034-journald-accept-EPOLLERR-from-dev-kmsg.patch
Patch0035: 0035-journald-avoid-NSS-in-journald.patch
Patch0036: 0036-libudev-add-missing-global-to-symbol-export.patch
Patch0037: 0037-gpt-auto-generator-do-not-assume-that-dev-block-u-u-.patch
Patch0038: 0038-logind-put-correct-user-object-paths-in-introspectio.patch
Patch0039: 0039-Fix-obsolete-references-to-systemd-random-seed-load..patch
Patch0040: 0040-cgroup-always-enable-memory.use_hierarchy-for-all-cg.patch
Patch0041: 0041-journalctl-1-s-adm-systemd-journal.patch
Patch0042: 0042-cgroup-if-we-do-a-cgroup-operation-then-do-something.patch
Patch0043: 0043-core-rework-how-we-match-mount-units-against-each-ot.patch
Patch0044: 0044-logind-never-consider-a-closing-session-relevant-for.patch
Patch0045: 0045-man-drop-references-to-cgroup-wher-appropriate.patch
Patch0046: 0046-systemctl-make-sure-set-property-mangles-unit-names.patch
Patch0047: 0047-dbus-fix-introspection-for-TimerSlackNSec.patch
Patch0048: 0048-swap-properly-expose-timeout-property-on-the-bus.patch
Patch0049: 0049-build-sys-restore-detection-of-sphinx.patch
Patch0050: 0050-util-add-macro-for-iterating-through-all-prefixes-of.patch
Patch0051: 0051-util-properly-handle-the-root-dir-in-PATH_FOREACH_PR.patch
Patch0052: 0052-cgroup-get-rid-of-MemorySoftLimit.patch
Patch0053: 0053-set-IgnoreOnIsolate-true-for-systemd-cryptsetup-.ser.patch
Patch0054: 0054-main-don-t-free-fds-array-twice.patch
Patch0055: 0055-local-fix-memory-leak-when-putting-together-locale-s.patch
Patch0056: 0056-hashmap-size-hashmap-bucket-array-dynamically.patch
Patch0057: 0057-smack-setup-fix-path-to-Smack-CIPSO-mappings.patch
Patch0058: 0058-fix-lingering-references-to-var-lib-backlight-random.patch
Patch0059: 0059-cryptsetup-fix-OOM-handling-when-parsing-mount-optio.patch
Patch0060: 0060-journald-add-missing-error-check.patch
Patch0061: 0061-bus-fix-potentially-uninitialized-memory-access.patch
Patch0062: 0062-dbus-fix-return-value-of-dispatch_rqueue.patch
Patch0063: 0063-modules-load-fix-error-handling.patch
Patch0064: 0064-efi-never-call-qsort-on-potentially-NULL-arrays.patch
Patch0065: 0065-strv-don-t-access-potentially-NULL-string-arrays.patch
Patch0066: 0066-mkdir-pass-a-proper-function-pointer-to-mkdir_safe_i.patch
Patch0067: 0067-tmpfiles.d-include-setgid-perms-for-run-log-journal.patch
Patch0068: 0068-gpt-auto-generator-exit-immediately-if-in-container.patch
Patch0069: 0069-systemd-order-remote-mounts-from-mountinfo-before-re.patch
Patch0070: 0070-manager-when-verifying-whether-clients-may-change-en.patch
Patch0071: 0071-mount-check-for-NULL-before-reading-pm-what.patch
Patch0072: 0072-core-do-not-add-what-to-RequiresMountsFor-for-networ.patch
Patch0073: 0073-systemd-serialize-deserialize-forbid_restart-value.patch
Patch0074: 0074-core-unify-the-way-we-denote-serialization-attribute.patch
Patch0075: 0075-journald-fix-minor-memory-leak.patch
Patch0076: 0076-journald-remove-rotated-file-from-hashmap-when-rotat.patch
Patch0077: 0077-udevadm.xml-document-resolve-names-option-for-test.patch
Patch0078: 0078-dbus-common-avoid-leak-in-error-path.patch
Patch0079: 0079-drop-ins-check-return-value.patch
Patch0080: 0080-shared-util-Fix-glob_extend-argument.patch
Patch0081: 0081-Fix-for-SIGSEGV-in-systemd-bootchart-on-short-living.patch
Patch0082: 0082-man-document-the-b-special-boot-option.patch
Patch0083: 0083-tmpfiles-log-unaccessible-FUSE-mount-points-only-as-.patch
Patch0084: 0084-move-utf8-functions-from-libudev-private.h-to-utf8.h.patch
Patch0085: 0085-Use-udev_encode_string-in-fstab_node_to_udev_node.patch
Patch0086: 0086-Fix-buffer-overrun-when-enumerating-files.patch
Patch0087: 0087-shared-utf8-merge-implementations-remove-cruft.patch
Patch0088: 0088-device-nodes-move-device-node-specific-code-to-own-f.patch
Patch0089: 0089-shared-util-fix-off-by-one-error-in-tag_to_udev_node.patch
Patch0090: 0090-udev-path_id-fix-by-path-link-generation-for-scm-dev.patch
Patch0091: 0091-hashmap-randomize-hash-functions-a-bit.patch
Patch0092: 0092-Configurable-Timeouts-Restarts-default-values.patch
Patch0093: 0093-manager-configurable-StartLimit-default-values.patch
Patch0094: 0094-sysctl-bring-back-etc-sysctl.conf.patch
Patch0095: 0095-tmpfiles-add-a-new-m-line-type-that-adjusts-user-gro.patch
Patch0096: 0096-systemd-treat-reload-failure-as-failure.patch
Patch0097: 0097-journal-when-appending-to-journal-file-allocate-larg.patch
Patch0098: 0098-journal-optimize-bisection-logic-a-bit-by-caching-th.patch
Patch0099: 0099-journal-fix-iteration-when-we-go-backwards-from-the-.patch
Patch0100: 0100-journal-allow-journal_file_copy_entry-to-work-on-non.patch
Patch0101: 0101-journal-simplify-pre-allocation-logic.patch
Patch0102: 0102-journald-mention-how-long-we-needed-to-flush-to-var-.patch
Patch0103: 0103-Never-call-qsort-on-potentially-NULL-arrays.patch
Patch0104: 0104-localed-match-converted-keymaps-before-legacy.patch
Patch0105: 0105-core-socket-fix-SO_REUSEPORT.patch
Patch0106: 0106-activate-fix-crash-when-s-is-passed.patch
Patch0107: 0107-systemd-python-fix-booted-and-add-two-functions-to-d.patch
Patch0108: 0108-util.c-check-if-return-value-from-ttyname_r-is-0-ins.patch
Patch0109: 0109-activate-mention-E-in-the-help-text.patch
Patch0110: 0110-docs-remove-unneeded-the-s-in-gudev-docs.patch
Patch0111: 0111-man-explicitly-say-when-multiple-units-can-be-specif.patch
Patch0112: 0112-util-fix-handling-of-trailing-whitespace-in-split_qu.patch
Patch0113: 0113-man-Improve-the-description-of-parameter-X-in-tmpfil.patch
Patch0114: 0114-cgroup_show-don-t-call-show_pid_array-on-empty-array.patch

%global num_patches %{lua: c=0; for i,p in ipairs(patches) do c=c+1; end; print(c);}

BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  dbus-devel
BuildRequires:  libacl-devel
BuildRequires:  pciutils-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libblkid-devel
BuildRequires:  xz-devel
BuildRequires:  kmod-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  qrencode-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  python2-devel
%if %{num_patches}
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  git
%endif
Requires(post): coreutils
Requires(post): gawk
Requires(post): sed
Requires(post): acl
Requires(pre):  coreutils
Requires(pre):  /usr/bin/getent
Requires(pre):  /usr/sbin/groupadd
Requires:       dbus
Requires:       nss-myhostname
Requires:       %{name}-libs = %{version}-%{release}
Requires:       kmod >= 14

Provides:       /bin/systemctl
Provides:       /sbin/shutdown
Provides:       syslog
Provides:       systemd-units = %{version}-%{release}
# part of system since f18, drop at f20
Provides:       udev = %{version}
Obsoletes:      udev < 183
Conflicts:      dracut < 027
# f18 version, drop at f20
Conflicts:      plymouth < 0.8.5.1
# For the journal-gateway split in F20, drop at F22
Obsoletes:      systemd < 204-10
# Ensures correct multilib updates added F18, drop at F20
Conflicts:      systemd < 185-4
# added F18, drop at F20
Obsoletes:      system-setup-keyboard < 0.9
Provides:       system-setup-keyboard = 0.9
# nss-myhostname got integrated in F19, drop at F21
Obsoletes:      nss-myhostname < 0.4
Provides:       nss-myhostname = 0.4
# systemd-analyze got merged in F19, drop at F21
Obsoletes:      systemd-analyze < 198
Provides:       systemd-analyze = 198
Obsoletes:      upstart < 1.2-3
Obsoletes:      upstart-sysvinit < 1.2-3
Conflicts:      upstart-sysvinit
Obsoletes:      hal
Obsoletes:      ConsoleKit

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package libs
Summary:        systemd libraries
License:        LGPLv2+ and MIT
Obsoletes:      libudev < 183
Obsoletes:      systemd < 185-4
Conflicts:      systemd < 185-4

%description libs
Libraries for systemd and udev, as well as the systemd PAM module.

%package devel
Summary:        Development headers for systemd
License:        LGPLv2+ and MIT
Requires:       %{name} = %{version}-%{release}
Provides:       libudev-devel = %{version}
Obsoletes:      libudev-devel < 183

%description devel
Development headers and auxiliary files for developing applications for systemd.

%package sysv
Summary:        SysV tools for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description sysv
SysV compatibility tools for systemd

%package python
Summary:        Python Bindings for systemd
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description python
This package contains python binds for systemd APIs

%package -n libgudev1
Summary:        Libraries for adding libudev support to applications that use glib
Conflicts:      filesystem < 3
License:        LGPLv2+
Requires:       %{name} = %{version}-%{release}

%description -n libgudev1
This package contains the libraries that make it easier to use libudev
functionality from applications that use glib.

%package -n libgudev1-devel
Summary:        Header files for adding libudev support to applications that use glib
Requires:       libgudev1 = %{version}-%{release}
License:        LGPLv2+

%description -n libgudev1-devel
This package contains the header and pkg-config files for developing
glib-based applications using libudev functionality.

%package journal-gateway
Summary:        Gateway for serving journal events over the network using HTTP
Requires:       %{name} = %{version}-%{release}
License:        LGPLv2+
Requires(pre):    /usr/bin/getent
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# For the journal-gateway split in F20, drop at F22
Obsoletes:      systemd < 204-10

%description journal-gateway
systemd-journal-gatewayd serves journal events over the network using HTTP.

%prep
%setup -q 

%if %{num_patches}
    git init
    git config user.email "systemd-maint@redhat.com"
    git config user.name "Fedora systemd team"
    git add .
    git commit -a -q -m "%{version} baseline."

    # Apply all the patches.
    git am \
        --exclude .gitignore \
        --exclude docs/.gitignore \
        --exclude docs/gudev/.gitignore \
        --exclude docs/libudev/.gitignore \
        --exclude docs/sysvinit/.gitignore \
        --exclude docs/var-log/.gitignore \
        --exclude hwdb/.gitignore \
        --exclude m4/.gitignore \
        --exclude man/.gitignore \
        --exclude po/.gitignore \
        --exclude rules/.gitignore \
        --exclude src/.gitignore \
        --exclude src/analyze/.gitignore \
        --exclude src/core/.gitignore \
        --exclude src/gudev/.gitignore \
        --exclude src/hostname/.gitignore \
        --exclude src/journal/.gitignore \
        --exclude src/libsystemd-daemon/.gitignore \
        --exclude src/libsystemd-id128/.gitignore \
        --exclude src/libudev/.gitignore \
        --exclude src/locale/.gitignore \
        --exclude src/login/.gitignore \
        --exclude src/python-systemd/.gitignore \
        --exclude src/python-systemd/docs/* \
        --exclude src/timedate/.gitignore \
        --exclude src/udev/.gitignore \
        --exclude src/udev/scsi_id/.gitignore \
        --exclude sysctl.d/.gitignore \
        --exclude test/.gitignore \
        --exclude units/.gitignore \
        --exclude units/user/.gitignore \
        %{patches}
%endif

%build
%if %{num_patches}
    autoreconf
%endif

%configure \
        --libexecdir=%{_prefix}/lib \
        --enable-gtk-doc \
        --disable-static \
        --with-sysvinit-path=/etc/rc.d/init.d \
        --with-rc-local-script-path-start=/etc/rc.d/rc.local
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -delete

# udev links
mkdir -p %{buildroot}/%{_sbindir}
ln -sf ../bin/udevadm %{buildroot}%{_sbindir}/udevadm

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
ln -s ../lib/systemd/systemd %{buildroot}%{_sbindir}/init
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/reboot
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/halt
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/poweroff
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/shutdown
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/telinit
ln -s ../bin/systemctl %{buildroot}%{_sbindir}/runlevel

# legacy links
ln -s loginctl %{buildroot}%{_bindir}/systemd-loginctl

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}%{_sysconfdir}/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/syslog.target.wants

# Make sure the user generators dir exists too
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-generators
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-generators

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/localtime
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Install Fedora default preset policy
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-preset/
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE7} %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Make sure the shutdown/sleep drop-in dirs exist
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-shutdown/
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep/

# Make sure the NTP units dir exists
mkdir -p %{buildroot}%{_prefix}/lib/systemd/ntp-units.d/

# Make sure directories in /var exist
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/coredump
mkdir -p %{buildroot}%{_localstatedir}/lib/systemd/catalog
touch %{buildroot}%{_localstatedir}/lib/systemd/catalog/database
touch %{buildroot}%{_sysconfdir}/udev/hwdb.bin

# Install SysV conversion tool for systemd
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/

# Install rsyslog fragment
mkdir -p %{buildroot}%{_sysconfdir}/rsyslog.d/
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/rsyslog.d/

# Install yum protection fragment
mkdir -p %{buildroot}%{_sysconfdir}/yum/protected.d/
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/yum/protected.d/systemd.conf

# Install rc.local
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/
install -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/rc.d/rc.local
ln -s rc.d/rc.local %{buildroot}%{_sysconfdir}/rc.local

# To avoid making life hard for Rawhide-using developers, don't package the
# kernel.core_pattern setting until systemd-coredump is a part of an actual
# systemd release and it's made clear how to get the core dumps out of the
# journal.
rm -f %{buildroot}%{_prefix}/lib/sysctl.d/50-coredump.conf

# For now remove /var/log/README since we are not enabling persistant
# logging yet.
rm -f %{buildroot}%{_localstatedir}/log/README

# No tmp-on-tmpfs by default in RHEL7. bz#876122
rm -f %{buildroot}%{_prefix}/lib/systemd/system/local-fs.target.wants/tmp.mount

# No gpt-auto-generator in RHEL7
rm -f %{buildroot}%{_prefix}/lib/systemd/system-generators/systemd-gpt-auto-generator

%pre
getent group cdrom >/dev/null 2>&1 || groupadd -r -g 11 cdrom >/dev/null 2>&1 || :
getent group tape >/dev/null 2>&1 || groupadd -r -g 33 tape >/dev/null 2>&1 || :
getent group dialout >/dev/null 2>&1 || groupadd -r -g 18 dialout >/dev/null 2>&1 || :
getent group floppy >/dev/null 2>&1 || groupadd -r -g 19 floppy >/dev/null 2>&1 || :
getent group systemd-journal >/dev/null 2>&1 || groupadd -r -g 190 systemd-journal 2>&1 || :

systemctl stop systemd-udevd-control.socket systemd-udevd-kernel.socket systemd-udevd.service >/dev/null 2>&1 || :

# Rename configuration files that changed their names
mv -n %{_sysconfdir}/systemd/systemd-logind.conf %{_sysconfdir}/systemd/logind.conf >/dev/null 2>&1 || :
mv -n %{_sysconfdir}/systemd/systemd-journald.conf %{_sysconfdir}/systemd/journald.conf >/dev/null 2>&1 || :

%pretrans -p <lua>
--# Migrate away from systemd-timedated-ntp.target.
--# Take note which ntp services, if any, were pulled in by it.
--# We'll enable them the usual way in %%post.
--# Remove this after upgrades from F17 are no longer supported.
function migrate_ntp()
    --# Are we upgrading from a version that had systemd-timedated-ntp.target?
    t = posix.stat("/usr/lib/systemd/system/systemd-timedated-ntp.target", "type")
    if t ~= "regular" then return end

    --# Was the target enabled?
    t = posix.stat("/etc/systemd/system/multi-user.target.wants/systemd-timedated-ntp.target", "type")
    if t ~= "link" then return end

    --# filesystem provides /var/lib/rpm-state since F17 GA
    r,msg,errno = posix.mkdir("/var/lib/rpm-state/systemd")
    if r == nil and errno ~= 17 then return end  --# EEXIST is fine.

    --# Save the list of ntp services pulled by the target.
    f = io.open("/var/lib/rpm-state/systemd/ntp-units", "w")
    if f == nil then return end

    files = posix.dir("/usr/lib/systemd/system/systemd-timedated-ntp.target.wants")
    for i,name in ipairs(files) do
        if name ~= "." and name ~= ".." then
            s = string.format("%s\n", name)
            f:write(s)
        end
    end

    f:close()
end

migrate_ntp()
return 0

%post
systemd-machine-id-setup >/dev/null 2>&1 || :
/usr/lib/systemd/systemd-random-seed save >/dev/null 2>&1 || :
systemctl daemon-reexec >/dev/null 2>&1 || :
systemctl start systemd-udevd.service >/dev/null 2>&1 || :
udevadm hwdb --update >/dev/null 2>&1 || :
journalctl --update-catalog >/dev/null 2>&1 || :

# Stop-gap until rsyslog.rpm does this on its own. (This is supposed
# to fail when the link already exists)
ln -s /usr/lib/systemd/system/rsyslog.service /etc/systemd/system/syslog.service >/dev/null 2>&1 || :

if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/usr/lib/systemd/system/graphical.target"
        else
                target="/usr/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        ln -sf "$target" /etc/systemd/system/default.target >/dev/null 2>&1 || :

        # Services we install by default, and which are controlled by presets.
        systemctl preset \
                getty@tty1.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :
else
        # This systemd service does not exist anymore, we now do it
        # internally in PID 1
        rm -f /etc/systemd/system/sysinit.target.wants/hwclock-load.service >/dev/null 2>&1 || :

        # This systemd target does not exist anymore. It's been replaced
        # by ntp-units.d.
        rm -f /etc/systemd/system/multi-user.target.wants/systemd-timedated-ntp.target >/dev/null 2>&1 || :

        # Enable the units recorded by %%pretrans
        if [ -e /var/lib/rpm-state/systemd/ntp-units ] ; then
                while read service; do
                        systemctl enable "$service" >/dev/null 2>&1 || :
                done < /var/lib/rpm-state/systemd/ntp-units
                rm -r /var/lib/rpm-state/systemd/ntp-units >/dev/null 2>&1 || :
        fi
fi

# Migrate /etc/sysconfig/clock
if [ ! -L /etc/localtime -a -e /etc/sysconfig/clock ] ; then
       . /etc/sysconfig/clock >/dev/null 2>&1 || :
       if [ -n "$ZONE" -a -e "/usr/share/zoneinfo/$ZONE" ] ; then
              ln -sf "../usr/share/zoneinfo/$ZONE" /etc/localtime >/dev/null 2>&1 || :
       fi
fi
rm -f /etc/sysconfig/clock >/dev/null 2>&1 || :

# Migrate /etc/sysconfig/i18n
if [ -e /etc/sysconfig/i18n -a ! -e /etc/locale.conf ]; then
        unset LANG
        unset LC_CTYPE
        unset LC_NUMERIC
        unset LC_TIME
        unset LC_COLLATE
        unset LC_MONETARY
        unset LC_MESSAGES
        unset LC_PAPER
        unset LC_NAME
        unset LC_ADDRESS
        unset LC_TELEPHONE
        unset LC_MEASUREMENT
        unset LC_IDENTIFICATION
        . /etc/sysconfig/i18n >/dev/null 2>&1 || :
        [ -n "$LANG" ] && echo LANG=$LANG > /etc/locale.conf 2>&1 || :
        [ -n "$LC_CTYPE" ] && echo LC_CTYPE=$LC_CTYPE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_NUMERIC" ] && echo LC_NUMERIC=$LC_NUMERIC >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_TIME" ] && echo LC_TIME=$LC_TIME >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_COLLATE" ] && echo LC_COLLATE=$LC_COLLATE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MONETARY" ] && echo LC_MONETARY=$LC_MONETARY >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MESSAGES" ] && echo LC_MESSAGES=$LC_MESSAGES >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_PAPER" ] && echo LC_PAPER=$LC_PAPER >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_NAME" ] && echo LC_NAME=$LC_NAME >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_ADDRESS" ] && echo LC_ADDRESS=$LC_ADDRESS >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_TELEPHONE" ] && echo LC_TELEPHONE=$LC_TELEPHONE >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_MEASUREMENT" ] && echo LC_MEASUREMENT=$LC_MEASUREMENT >> /etc/locale.conf 2>&1 || :
        [ -n "$LC_IDENTIFICATION" ] && echo LC_IDENTIFICATION=$LC_IDENTIFICATION >> /etc/locale.conf 2>&1 || :
fi

# Migrate /etc/sysconfig/keyboard
if [ -e /etc/sysconfig/keyboard -a ! -e /etc/vconsole.conf ]; then
        unset SYSFONT
        unset SYSFONTACM
        unset UNIMAP
        unset KEYMAP
        [ -e /etc/sysconfig/i18n ] && . /etc/sysconfig/i18n >/dev/null 2>&1 || :
        . /etc/sysconfig/keyboard >/dev/null 2>&1 || :
        [ -n "$SYSFONT" ] && echo FONT=$SYSFONT > /etc/vconsole.conf 2>&1 || :
        [ -n "$SYSFONTACM" ] && echo FONT_MAP=$SYSFONTACM >> /etc/vconsole.conf 2>&1 || :
        [ -n "$UNIMAP" ] && echo FONT_UNIMAP=$UNIMAP >> /etc/vconsole.conf 2>&1 || :
        [ -n "$KEYTABLE" ] && echo KEYMAP=$KEYTABLE >> /etc/vconsole.conf 2>&1 || :
fi
rm -f /etc/sysconfig/i18n >/dev/null 2>&1 || :
rm -f /etc/sysconfig/keyboard >/dev/null 2>&1 || :

# Migrate HOSTNAME= from /etc/sysconfig/network
if [ -e /etc/sysconfig/network -a ! -e /etc/hostname ]; then
        unset HOSTNAME
        . /etc/sysconfig/network >/dev/null 2>&1 || :
        [ -n "$HOSTNAME" ] && echo $HOSTNAME > /etc/hostname 2>&1 || :
fi
sed -i '/^HOSTNAME=/d' /etc/sysconfig/network >/dev/null 2>&1 || :

# Migrate the old systemd-setup-keyboard X11 configuration fragment
if [ ! -e /etc/X11/xorg.conf.d/00-keyboard.conf ] ; then
        mv /etc/X11/xorg.conf.d/00-system-setup-keyboard.conf /etc/X11/xorg.conf.d/00-keyboard.conf >/dev/null 2>&1 || :
else
        rm -f /etc/X11/xorg.conf.d/00-system-setup-keyboard.conf >/dev/null 2>&1 || :
fi

# sed-fu to add myhostname to the hosts line of /etc/nsswitch.conf
if [ -f /etc/nsswitch.conf ] ; then
        sed -i.bak -e '
                /^hosts:/ !b
                /\<myhostname\>/ b
                s/[[:blank:]]*$/ myhostname/
                ' /etc/nsswitch.conf >/dev/null 2>&1 || :
fi

%posttrans
# Convert old /etc/sysconfig/desktop settings
preferred=
if [ -f /etc/sysconfig/desktop ]; then
        . /etc/sysconfig/desktop
        if [ "$DISPLAYMANAGER" = GNOME ]; then
                preferred=gdm
        elif [ "$DISPLAYMANAGER" = KDE ]; then
                preferred=kdm
        elif [ "$DISPLAYMANAGER" = WDM ]; then
                preferred=wdm
        elif [ "$DISPLAYMANAGER" = XDM ]; then
                preferred=xdm
        elif [ -n "$DISPLAYMANAGER" ]; then
                preferred=${DISPLAYMANAGER##*/}
        fi
fi
if [ -z "$preferred" ]; then
        if [ -x /usr/sbin/gdm ]; then
                preferred=gdm
        elif [ -x /usr/bin/kdm ]; then
                preferred=kdm
        fi
fi
if [ -n "$preferred" -a -r "/usr/lib/systemd/system/$preferred.service" ]; then
        # This is supposed to fail when the symlink already exists
        ln -s "/usr/lib/systemd/system/$preferred.service" /etc/systemd/system/display-manager.service >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
        systemctl daemon-reload > /dev/null 2>&1 || :
        systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
        systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :

        rm -f /etc/systemd/system/default.target >/dev/null 2>&1 || :

        if [ -f /etc/nsswitch.conf ] ; then
                sed -i.bak -e '
                        /^hosts:/ !b
                        s/[[:blank:]]\+myhostname\>//
                        ' /etc/nsswitch.conf >/dev/null 2>&1 || :
        fi
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post -n libgudev1 -p /sbin/ldconfig
%postun -n libgudev1 -p /sbin/ldconfig

%pre journal-gateway
getent group systemd-journal-gateway >/dev/null 2>&1 || groupadd -r -g 191 systemd-journal-gateway 2>&1 || :
getent passwd systemd-journal-gateway >/dev/null 2>&1 || useradd -r -l -u 191 -g systemd-journal-gateway -d %{_prefix}/lib/systemd -s /sbin/nologin -c "Journal Gateway" systemd-journal-gateway >/dev/null 2>&1 || :

%post journal-gateway
%systemd_post systemd-journal-gatewayd.socket systemd-journal-gatewayd.service

%preun journal-gateway
%systemd_preun systemd-journal-gatewayd.socket systemd-journal-gatewayd.service

%postun journal-gateway
%systemd_postun_with_restart systemd-journal-gatewayd.service

%files
%doc %{_docdir}/systemd
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/udev
%dir %{_sysconfdir}/udev/rules.d
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/system-generators
%dir %{_prefix}/lib/systemd/user-generators
%dir %{_prefix}/lib/systemd/system-preset
%dir %{_prefix}/lib/systemd/user-preset
%dir %{_prefix}/lib/systemd/system-shutdown
%dir %{_prefix}/lib/systemd/system-sleep
%dir %{_prefix}/lib/systemd/catalog
%dir %{_prefix}/lib/systemd/ntp-units.d
%dir %{_prefix}/lib/tmpfiles.d
%dir %{_prefix}/lib/sysctl.d
%dir %{_prefix}/lib/modules-load.d
%dir %{_prefix}/lib/binfmt.d
%dir %{_datadir}/systemd
%dir %{_datadir}/pkgconfig
%dir %{_localstatedir}/lib/systemd
%dir %{_localstatedir}/lib/systemd/catalog
%dir %{_localstatedir}/lib/systemd/coredump
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.machine1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/logind.conf
%config(noreplace) %{_sysconfdir}/systemd/journald.conf
%config(noreplace) %{_sysconfdir}/systemd/bootchart.conf
%config(noreplace) %{_sysconfdir}/udev/udev.conf
%config(noreplace) %{_sysconfdir}/rsyslog.d/listen.conf
%config(noreplace) %{_sysconfdir}/yum/protected.d/systemd.conf
%config(noreplace) %{_sysconfdir}/pam.d/systemd-user
%ghost %{_sysconfdir}/udev/hwdb.bin
%{_rpmconfigdir}/macros.d/macros.systemd
%{_sysconfdir}/xdg/systemd
%{_sysconfdir}/rc.d/init.d/README
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/localtime
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-system-setup-keyboard.conf
%ghost %{_localstatedir}/lib/systemd/catalog/database
%{_bindir}/systemctl
%{_bindir}/systemd-notify
%{_bindir}/systemd-analyze
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/systemd-machine-id-setup
%{_bindir}/loginctl
%{_bindir}/systemd-loginctl
%{_bindir}/journalctl
%{_bindir}/machinectl
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-run
%caps(cap_dac_override,cap_sys_ptrace=pe) %{_bindir}/systemd-detect-virt
%{_bindir}/systemd-inhibit
%{_bindir}/hostnamectl
%{_bindir}/localectl
%{_bindir}/timedatectl
%{_bindir}/bootctl
%{_bindir}/systemd-coredumpctl
%{_bindir}/udevadm
%{_bindir}/kernel-install
%{_prefix}/lib/systemd/systemd
%exclude %{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/system
%{_prefix}/lib/systemd/user
%exclude %{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_prefix}/lib/systemd/systemd-*
%{_prefix}/lib/udev
%{_prefix}/lib/systemd/system-generators/systemd-cryptsetup-generator
%{_prefix}/lib/systemd/system-generators/systemd-getty-generator
%{_prefix}/lib/systemd/system-generators/systemd-rc-local-generator
%{_prefix}/lib/systemd/system-generators/systemd-fstab-generator
%{_prefix}/lib/systemd/system-generators/systemd-system-update-generator
%{_prefix}/lib/systemd/system-generators/systemd-efi-boot-generator
%{_prefix}/lib/tmpfiles.d/systemd.conf
%{_prefix}/lib/tmpfiles.d/x11.conf
%{_prefix}/lib/tmpfiles.d/legacy.conf
%{_prefix}/lib/tmpfiles.d/tmp.conf
%{_prefix}/lib/sysctl.d/50-default.conf
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%{_prefix}/lib/systemd/catalog/systemd.catalog
%{_prefix}/lib/kernel/install.d/50-depmod.install
%{_prefix}/lib/kernel/install.d/90-loaderentry.install
%{_sbindir}/init
%{_sbindir}/reboot
%{_sbindir}/halt
%{_sbindir}/poweroff
%{_sbindir}/shutdown
%{_sbindir}/telinit
%{_sbindir}/runlevel
%{_sbindir}/udevadm
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%exclude %{_mandir}/man8/systemd-journal-gatewayd.*
%{_mandir}/man8/*
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.machine1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%{_datadir}/pkgconfig/systemd.pc
%{_datadir}/pkgconfig/udev.pc
%{_datadir}/bash-completion/completions/hostnamectl
%{_datadir}/bash-completion/completions/journalctl
%{_datadir}/bash-completion/completions/localectl
%{_datadir}/bash-completion/completions/loginctl
%{_datadir}/bash-completion/completions/systemctl
%{_datadir}/bash-completion/completions/systemd-coredumpctl
%{_datadir}/bash-completion/completions/timedatectl
%{_datadir}/bash-completion/completions/udevadm
%{_datadir}/bash-completion/completions/systemd-analyze
%{_datadir}/bash-completion/completions/kernel-install
%{_datadir}/bash-completion/completions/systemd-run
%{_datadir}/zsh/site-functions/*
%ghost %{_localstatedir}/lib/random-seed
%ghost %dir %{_localstatedir}/var/lib/systemd/
%ghost %dir %{_localstatedir}/var/lib/systemd/coredump
%ghost %dir %{_localstatedir}/var/lib/systemd/catalog
%ghost %{_localstatedir}/var/lib/systemd/catalog/database
%ghost %dir %{_localstatedir}/var/lib/backlight/
%config(noreplace) %{_sysconfdir}/rc.d/rc.local
%{_sysconfdir}/rc.local

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files libs
%{_libdir}/security/pam_systemd.so
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libsystemd-daemon.so.*
%{_libdir}/libsystemd-login.so.*
%{_libdir}/libsystemd-journal.so.*
%{_libdir}/libsystemd-id128.so.*
%{_libdir}/libudev.so.*

%files devel
%dir %{_includedir}/systemd
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_libdir}/libsystemd-journal.so
%{_libdir}/libsystemd-id128.so
%{_libdir}/libudev.so
%{_includedir}/systemd/sd-daemon.h
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-journal.h
%{_includedir}/systemd/sd-id128.h
%{_includedir}/systemd/sd-messages.h
%{_includedir}/systemd/sd-shutdown.h
%{_includedir}/libudev.h
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc
%{_libdir}/pkgconfig/libsystemd-journal.pc
%{_libdir}/pkgconfig/libsystemd-id128.pc
%{_libdir}/pkgconfig/libudev.pc
%{_mandir}/man3/*
%dir %{_datadir}/gtk-doc/html/libudev
%{_datadir}/gtk-doc/html/libudev/*

%files sysv
%{_bindir}/systemd-sysv-convert

%files python
%{python_sitearch}/systemd/__init__.py
%{python_sitearch}/systemd/__init__.pyc
%{python_sitearch}/systemd/__init__.pyo
%{python_sitearch}/systemd/_journal.so
%{python_sitearch}/systemd/_reader.so
%{python_sitearch}/systemd/_daemon.so
%{python_sitearch}/systemd/id128.so
%{python_sitearch}/systemd/login.so
%{python_sitearch}/systemd/journal.py
%{python_sitearch}/systemd/journal.pyc
%{python_sitearch}/systemd/journal.pyo
%{python_sitearch}/systemd/daemon.py
%{python_sitearch}/systemd/daemon.pyc
%{python_sitearch}/systemd/daemon.pyo

%files -n libgudev1
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files -n libgudev1-devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*

%files journal-gateway
%{_prefix}/lib/systemd/system/systemd-journal-gatewayd.*
%{_prefix}/lib/systemd/systemd-journal-gatewayd
%{_mandir}/man8/systemd-journal-gatewayd.*
%{_datadir}/systemd/gatewayd

%changelog
* Thu Dec 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-10
- cgroup_show: don't call show_pid_array on empty arrays

* Wed Dec 18 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-9
- treat reload failure as failure (#1036848)
- improve journal performance (#1029604)
- backport bugfixes (#1043525)
- fix handling of trailing whitespace in split_quoted (#984832)
- localed: match converted keymaps before legacy (#903776)
- improve the description of parameter X in tmpfiles.d page (#1029604)
- obsolete ConsoleKit (#1039761)
- make rc.local more backward comaptible (#1039465)

* Tue Nov 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-8
- tmpfiles: introduce m (#1030961)

* Tue Nov 12 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-7
- introduce DefaultStartLimit (#821723)

* Mon Nov 11 2013 Harald Hoyer <harald@redhat.com> 207-6
- changed systemd-journal-gateway login shell to /sbin/nologin
- backported a lot of bugfixes
- udev: path_id - fix by-path link generation for scm devices
Resolves: rhbz#888707

* Tue Nov 05 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-5
- create /etc/rc.d/rc.local (#968401)
- cgroup: always enable memory.use_hierarchy= for all cgroups (#1011575)
- remove user@.service (#1019738)
- drop some out-of-date references to cgroup settings (#1000004)
- explain NAME in systemctl man page (#978954)

* Tue Oct 15 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-4
- core: whenever a new PID is passed to us, make sure we watch it

* Tue Oct 01 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-3
- presets: add tuned.service

* Thu Sep 19 2013 Lukas Nykryn <lnykryn@redhat.com> - 207-2
- Advertise hibernation only if there's enough free swap
- swap: create .wants symlink to 'auto' swap devices
- Verify validity of session name when received from outside
- polkit: Avoid race condition in scraping /proc
Resolves: rhbz#1005142

* Fri Sep 13 2013 Harald Hoyer <harald@redhat.com> 207-1
- version 207

* Fri Sep 06 2013 Harald Hoyer <harald@redhat.com> 206-8
- support "debug" kernel command line parameter
- journald: fix fd leak in journal_file_empty
- journald: fix vacuuming of archived journals
- libudev: enumerate - do not try to match against an empty subsystem
- cgtop: fixup the online help
- libudev: fix memleak when enumerating childs

* Wed Aug 28 2013 Harald Hoyer <harald@redhat.com> 206-7
- fixed cgroup hashmap corruption
Resolves: rhbz#997742 rhbz#995197

* Fri Aug 23 2013 Harald Hoyer <harald@redhat.com> 206-6
- cgroup.c: check return value of unit_realize_cgroup_now()
Resolves: rhbz#997742 rhbz#995197

* Thu Aug 22 2013 Harald Hoyer <harald@redhat.com> 206-5
- obsolete upstart
Resolves: rhbz#978014
- obsolete hal
Resolves: rhbz#975589
- service: always unwatch PIDs before forgetting old ones
Resolves: rhbz#995197
- units: disable kmod-static-nodes.service in containers
- use CAP_MKNOD ConditionCapability
- fstab-generator: read rd.fstab=on/off switch correctly
- backlight: add minimal tool to save/restore screen brightness
- backlight: instead of syspath use sysname for identifying
- sysctl: allow overwriting of values specified in "later"
- systemd-python: fix initialization of _Reader objects
- udevd: simplify sigterm check
- libudev: fix hwdb validation to look for the *new* file
- units: make fsck units remain after exit
- udev: replace CAP_MKNOD by writable /sys condition
- libudev-enumerate.c:udev_enumerate_get_list_entry() fixed
- journal: fix parsing of facility in syslog messages

* Fri Aug 09 2013 Harald Hoyer <harald@redhat.com> 206-4
- journal: handle multiline syslog messages
- man: Fix copy&paste error
- core: synchronously block when logging
- journal: immediately sync to disk as soon as we receieve an EMERG/ALERT/CRIT message
- initctl: use irreversible jobs when switching runlevels
- udev: log error if chmod/chown of static dev nodes fails
- udev: static_node - don't touch permissions uneccessarily
- tmpfiles: support passing --prefix multiple times
- tmpfiles: introduce --exclude-prefix
- tmpfiles-setup: exclude /dev prefixes files
- logind: update state file after generating the session fifo, not before
- journalctl: use _COMM= match for scripts
- man: systemd.unit: fix volatile path
- man: link up scope+slice units from systemd.unit(5)
- man: there is no session mode, only user mode
- journal: fix hashmap leak in mmap-cache
- systemd-delta: Only print colors when on a tty
- systemd: fix segv in snapshot creation
- udev: hwdb - try reading modalias for usb before falling back to the composed one
- udevd: respect the log-level set in /etc/udev/udev.conf
- fstab-generator: respect noauto/nofail when adding sysroot mount

* Fri Aug 02 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 206-3
- add dependency on kmod >= 14
- remove /var/log/journal to make journal non-persistant (#989750)
- add hypervkvpd.service to presets (#924321)

* Thu Aug 01 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 206-2
- 80-net-name-slot.rules: only rename network interfaces on ACTION==add

* Tue Jul 23 2013 Kay Sievers <kay@redhat.com> - 206-1
- New upstream release
  Resolves (#984152)

* Wed Jul  3 2013 Lennart Poettering <lpoetter@redhat.com> - 205-1
- New upstream release

* Wed Jun 26 2013 Michal Schmidt <mschmidt@redhat.com> 204-10
- Split systemd-journal-gateway subpackage (#908081).

* Mon Jun 24 2013 Michal Schmidt <mschmidt@redhat.com> 204-9
- Rename nm_dispatcher to NetworkManager-dispatcher in default preset (#977433)

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-8
- fix, which helps to sucessfully browse journals with
  duplicated seqnums

* Fri Jun 14 2013 Harald Hoyer <harald@redhat.com> 204-7
- fix duplicate message ID bug
Resolves: rhbz#974132

* Thu Jun 06 2013 Harald Hoyer <harald@redhat.com> 204-6
- introduce 99-default-disable.preset

* Thu Jun  6 2013 Lennart Poettering <lpoetter@redhat.com> - 204-5
- Rename 90-display-manager.preset to 85-display-manager.preset so that it actually takes precedence over 90-default.preset's "disable *" line (#903690)

* Tue May 28 2013 Harald Hoyer <harald@redhat.com> 204-4
- Fix kernel-install (#965897)

* Wed May 22 2013 Kay Sievers <kay@redhat.com> - 204-3
- Fix kernel-install (#965897)

* Thu May  9 2013 Lennart Poettering <lpoetter@redhat.com> - 204-2
- New upstream release
- disable isdn by default (#959793)

* Tue May 07 2013 Harald Hoyer <harald@redhat.com> 203-2
- forward port kernel-install-grubby.patch

* Tue May  7 2013 Lennart Poettering <lpoetter@redhat.com> - 203-1
- New upstream release

* Wed Apr 24 2013 Harald Hoyer <harald@redhat.com> 202-3
- fix ENOENT for getaddrinfo
- Resolves: rhbz#954012 rhbz#956035
- crypt-setup-generator: correctly check return of strdup
- logind-dbus: initialize result variable
- prevent library underlinking

* Fri Apr 19 2013 Harald Hoyer <harald@redhat.com> 202-2
- nspawn create empty /etc/resolv.conf if necessary
- python wrapper: add sd_journal_add_conjunction()
- fix s390 booting
- Resolves: rhbz#953217

* Thu Apr 18 2013 Lennart Poettering <lpoetter@redhat.com> - 202-1
- New upstream release

* Tue Apr 09 2013 Michal Schmidt <mschmidt@redhat.com> - 201-2
- Automatically discover whether to run autoreconf and add autotools and git
  BuildRequires based on the presence of patches to be applied.
- Use find -delete.

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 201-1
- New upstream release

* Mon Apr  8 2013 Lennart Poettering <lpoetter@redhat.com> - 200-4
- Update preset file

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-3
- Remove NetworkManager-wait-online.service from presets file again, it should default to off

* Fri Mar 29 2013 Lennart Poettering <lpoetter@redhat.com> - 200-2
- New upstream release

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-2
- Add NetworkManager-wait-online.service to the presets file

* Tue Mar 26 2013 Lennart Poettering <lpoetter@redhat.com> - 199-1
- New upstream release

* Mon Mar 18 2013 Michal Schmidt <mschmidt@redhat.com> 198-7
- Drop /usr/s?bin/ prefixes.

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-6
- run autogen to pickup all changes

* Fri Mar 15 2013 Harald Hoyer <harald@redhat.com> 198-5
- do not mount anything, when not running as pid 1
- add initrd.target for systemd in the initrd

* Wed Mar 13 2013 Harald Hoyer <harald@redhat.com> 198-4
- fix switch-root and local-fs.target problem
- patch kernel-install to use grubby, if available

* Fri Mar 08 2013 Harald Hoyer <harald@redhat.com> 198-3
- add Conflict with dracut < 026 because of the new switch-root isolate

* Thu Mar  7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-2
- Create required users

* Thu Mar 7 2013 Lennart Poettering <lpoetter@redhat.com> - 198-1
- New release
- Enable journal persistancy by default

* Sun Feb 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 197-3
- Bump for ARM

* Fri Jan 18 2013 Michal Schmidt <mschmidt@redhat.com> - 197-2
- Added qemu-guest-agent.service to presets (Lennart, #885406).
- Add missing pygobject3-base to systemd-analyze deps (Lennart).
- Do not require hwdata, it is all in the hwdb now (Kay).
- Drop dependency on dbus-python.

* Tue Jan  8 2013 Lennart Poettering <lpoetter@redhat.com> - 197-1
- New upstream release

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-4
- Enable rngd.service by default (#857765).

* Mon Dec 10 2012 Michal Schmidt <mschmidt@redhat.com> - 196-3
- Disable hardening on s390(x) because PIE is broken there and produces
  text relocations with __thread (#868839).

* Wed Dec 05 2012 Michal Schmidt <mschmidt@redhat.com> - 196-2
- added spice-vdagentd.service to presets (Lennart, #876237)
- BR cryptsetup-devel instead of the legacy cryptsetup-luks-devel provide name
  (requested by Milan Brož).
- verbose make to see the actual build flags

* Wed Nov 21 2012 Lennart Poettering <lpoetter@redhat.com> - 196-1
- New upstream release

* Tue Nov 20 2012 Lennart Poettering <lpoetter@redhat.com> - 195-8
- https://bugzilla.redhat.com/show_bug.cgi?id=873459
- https://bugzilla.redhat.com/show_bug.cgi?id=878093

* Thu Nov 15 2012 Michal Schmidt <mschmidt@redhat.com> - 195-7
- Revert udev killing cgroup patch for F18 Beta.
- https://bugzilla.redhat.com/show_bug.cgi?id=873576

* Fri Nov 09 2012 Michal Schmidt <mschmidt@redhat.com> - 195-6
- Fix cyclical dep between systemd and systemd-libs.
- Avoid broken build of test-journal-syslog.
- https://bugzilla.redhat.com/show_bug.cgi?id=873387
- https://bugzilla.redhat.com/show_bug.cgi?id=872638

* Thu Oct 25 2012 Kay Sievers <kay@redhat.com> - 195-5
- require 'sed', limit HOSTNAME= match

* Wed Oct 24 2012 Michal Schmidt <mschmidt@redhat.com> - 195-4
- add dmraid-activation.service to the default preset
- add yum protected.d fragment
- https://bugzilla.redhat.com/show_bug.cgi?id=869619
- https://bugzilla.redhat.com/show_bug.cgi?id=869717

* Wed Oct 24 2012 Kay Sievers <kay@redhat.com> - 195-3
- Migrate /etc/sysconfig/ i18n, keyboard, network files/variables to
  systemd native files

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-2
- Provide syslog because the journal is fine as a syslog implementation

* Tue Oct 23 2012 Lennart Poettering <lpoetter@redhat.com> - 195-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=831665
- https://bugzilla.redhat.com/show_bug.cgi?id=847720
- https://bugzilla.redhat.com/show_bug.cgi?id=858693
- https://bugzilla.redhat.com/show_bug.cgi?id=863481
- https://bugzilla.redhat.com/show_bug.cgi?id=864629
- https://bugzilla.redhat.com/show_bug.cgi?id=864672
- https://bugzilla.redhat.com/show_bug.cgi?id=864674
- https://bugzilla.redhat.com/show_bug.cgi?id=865128
- https://bugzilla.redhat.com/show_bug.cgi?id=866346
- https://bugzilla.redhat.com/show_bug.cgi?id=867407
- https://bugzilla.redhat.com/show_bug.cgi?id=868603

* Wed Oct 10 2012 Michal Schmidt <mschmidt@redhat.com> - 194-2
- Add scriptlets for migration away from systemd-timedated-ntp.target

* Wed Oct  3 2012 Lennart Poettering <lpoetter@redhat.com> - 194-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=859614
- https://bugzilla.redhat.com/show_bug.cgi?id=859655

* Fri Sep 28 2012 Lennart Poettering <lpoetter@redhat.com> - 193-1
- New upstream release

* Tue Sep 25 2012 Lennart Poettering <lpoetter@redhat.com> - 192-1
- New upstream release

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-2
- Fix journal mmap header prototype definition to fix compilation on 32bit

* Fri Sep 21 2012 Lennart Poettering <lpoetter@redhat.com> - 191-1
- New upstream release
- Enable all display managers by default, as discussed with Adam Williamson

* Thu Sep 20 2012 Lennart Poettering <lpoetter@redhat.com> - 190-1
- New upstream release
- Take possession of /etc/localtime, and remove /etc/sysconfig/clock
- https://bugzilla.redhat.com/show_bug.cgi?id=858780
- https://bugzilla.redhat.com/show_bug.cgi?id=858787
- https://bugzilla.redhat.com/show_bug.cgi?id=858771
- https://bugzilla.redhat.com/show_bug.cgi?id=858754
- https://bugzilla.redhat.com/show_bug.cgi?id=858746
- https://bugzilla.redhat.com/show_bug.cgi?id=858266
- https://bugzilla.redhat.com/show_bug.cgi?id=858224
- https://bugzilla.redhat.com/show_bug.cgi?id=857670
- https://bugzilla.redhat.com/show_bug.cgi?id=856975
- https://bugzilla.redhat.com/show_bug.cgi?id=855863
- https://bugzilla.redhat.com/show_bug.cgi?id=851970
- https://bugzilla.redhat.com/show_bug.cgi?id=851275
- https://bugzilla.redhat.com/show_bug.cgi?id=851131
- https://bugzilla.redhat.com/show_bug.cgi?id=847472
- https://bugzilla.redhat.com/show_bug.cgi?id=847207
- https://bugzilla.redhat.com/show_bug.cgi?id=846483
- https://bugzilla.redhat.com/show_bug.cgi?id=846085
- https://bugzilla.redhat.com/show_bug.cgi?id=845973
- https://bugzilla.redhat.com/show_bug.cgi?id=845194
- https://bugzilla.redhat.com/show_bug.cgi?id=845028
- https://bugzilla.redhat.com/show_bug.cgi?id=844630
- https://bugzilla.redhat.com/show_bug.cgi?id=839736
- https://bugzilla.redhat.com/show_bug.cgi?id=835848
- https://bugzilla.redhat.com/show_bug.cgi?id=831740
- https://bugzilla.redhat.com/show_bug.cgi?id=823485
- https://bugzilla.redhat.com/show_bug.cgi?id=821813
- https://bugzilla.redhat.com/show_bug.cgi?id=807886
- https://bugzilla.redhat.com/show_bug.cgi?id=802198
- https://bugzilla.redhat.com/show_bug.cgi?id=767795
- https://bugzilla.redhat.com/show_bug.cgi?id=767561
- https://bugzilla.redhat.com/show_bug.cgi?id=752774
- https://bugzilla.redhat.com/show_bug.cgi?id=732874
- https://bugzilla.redhat.com/show_bug.cgi?id=858735

* Thu Sep 13 2012 Lennart Poettering <lpoetter@redhat.com> - 189-4
- Don't pull in pkg-config as dep
- https://bugzilla.redhat.com/show_bug.cgi?id=852828

* Wed Sep 12 2012 Lennart Poettering <lpoetter@redhat.com> - 189-3
- Update preset policy
- Rename preset policy file from 99-default.preset to 90-default.preset so that people can order their own stuff after the Fedora default policy if they wish

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-2
- Update preset policy
- https://bugzilla.redhat.com/show_bug.cgi?id=850814

* Thu Aug 23 2012 Lennart Poettering <lpoetter@redhat.com> - 189-1
- New upstream release

* Thu Aug 16 2012 Ray Strode <rstrode@redhat.com> 188-4
- more scriptlet fixes
  (move dm migration logic to %posttrans so the service
   files it's looking for are available at the time
   the logic is run)

* Sat Aug 11 2012 Lennart Poettering <lpoetter@redhat.com> - 188-3
- Remount file systems MS_PRIVATE before switching roots
- https://bugzilla.redhat.com/show_bug.cgi?id=847418

* Wed Aug 08 2012 Rex Dieter <rdieter@fedoraproject.org> - 188-2
- fix scriptlets

* Wed Aug  8 2012 Lennart Poettering <lpoetter@redhat.com> - 188-1
- New upstream release
- Enable gdm and avahi by default via the preset file
- Convert /etc/sysconfig/desktop to display-manager.service symlink
- Enable hardened build

* Mon Jul 30 2012 Kay Sievers <kay@redhat.com> - 187-3
- Obsolete: system-setup-keyboard

* Wed Jul 25 2012 Kalev Lember <kalevlember@gmail.com> - 187-2
- Run ldconfig for the new -libs subpackage

* Thu Jul 19 2012 Lennart Poettering <lpoetter@redhat.com> - 187-1
- New upstream release

* Mon Jul 09 2012 Harald Hoyer <harald@redhat.com> 186-2
- fixed dracut conflict version

* Tue Jul  3 2012 Lennart Poettering <lpoetter@redhat.com> - 186-1
- New upstream release

* Fri Jun 22 2012 Nils Philippsen <nils@redhat.com> - 185-7.gite7aee75
- add obsoletes/conflicts so multilib systemd -> systemd-libs updates work

* Thu Jun 14 2012 Michal Schmidt <mschmidt@redhat.com> - 185-6.gite7aee75
- Update to current git

* Wed Jun 06 2012 Kay Sievers - 185-5.gita2368a3
- disable plymouth in configure, to drop the .wants/ symlinks

* Wed Jun 06 2012 Michal Schmidt <mschmidt@redhat.com> - 185-4.gita2368a3
- Update to current git snapshot
  - Add systemd-readahead-analyze
  - Drop upstream patch
- Split systemd-libs
- Drop duplicate doc files
- Fixed License headers of subpackages

* Wed Jun 06 2012 Ray Strode <rstrode@redhat.com> - 185-3
- Drop plymouth files
- Conflict with old plymouth

* Tue Jun 05 2012 Kay Sievers - 185-2
- selinux udev labeling fix
- conflict with older dracut versions for new udev file names

* Mon Jun 04 2012 Kay Sievers - 185-1
- New upstream release
  - udev selinux labeling fixes
  - new man pages
  - systemctl help <unit name>

* Thu May 31 2012 Lennart Poettering <lpoetter@redhat.com> - 184-1
- New upstream release

* Thu May 24 2012 Kay Sievers <kay@redhat.com> - 183-1
- New upstream release including udev merge.

* Wed Mar 28 2012 Michal Schmidt <mschmidt@redhat.com> - 44-4
- Add triggers from Bill Nottingham to correct the damage done by
  the obsoleted systemd-units's preun scriptlet (#807457).

* Mon Mar 26 2012 Dennis Gilmore <dennis@ausil.us> - 44-3
- apply patch from upstream so we can build systemd on arm and ppc
- and likely the rest of the secondary arches

* Tue Mar 20 2012 Michal Schmidt <mschmidt@redhat.com> - 44-2
- Don't build the gtk parts anymore. They're moving into systemd-ui.
- Remove a dead patch file.

* Fri Mar 16 2012 Lennart Poettering <lpoetter@redhat.com> - 44-1
- New upstream release
- Closes #798760, #784921, #783134, #768523, #781735

* Mon Feb 27 2012 Dennis Gilmore <dennis@ausil.us> - 43-2
- don't conflict with fedora-release systemd never actually provided
- /etc/os-release so there is no actual conflict

* Wed Feb 15 2012 Lennart Poettering <lpoetter@redhat.com> - 43-1
- New upstream release
- Closes #789758, #790260, #790522

* Sat Feb 11 2012 Lennart Poettering <lpoetter@redhat.com> - 42-1
- New upstream release
- Save a bit of entropy during system installation (#789407)
- Don't own /etc/os-release anymore, leave that to fedora-release

* Thu Feb  9 2012 Adam Williamson <awilliam@redhat.com> - 41-2
- rebuild for fixed binutils

* Thu Feb  9 2012 Lennart Poettering <lpoetter@redhat.com> - 41-1
- New upstream release

* Tue Feb  7 2012 Lennart Poettering <lpoetter@redhat.com> - 40-1
- New upstream release

* Thu Jan 26 2012 Kay Sievers <kay@redhat.com> - 39-3
- provide /sbin/shutdown

* Wed Jan 25 2012 Harald Hoyer <harald@redhat.com> 39-2
- increment release

* Wed Jan 25 2012 Kay Sievers <kay@redhat.com> - 39-1.1
- install everything in /usr
  https://fedoraproject.org/wiki/Features/UsrMove

* Wed Jan 25 2012 Lennart Poettering <lpoetter@redhat.com> - 39-1
- New upstream release

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-6.git9fa2f41
- Update to a current git snapshot.
- Resolves: #781657

* Sun Jan 22 2012 Michal Schmidt <mschmidt@redhat.com> - 38-5
- Build against libgee06. Reenable gtk tools.
- Delete unused patches.
- Add easy building of git snapshots.
- Remove legacy spec file elements.
- Don't mention implicit BuildRequires.
- Configure with --disable-static.
- Merge -units into the main package.
- Move section 3 manpages to -devel.
- Fix unowned directory.
- Run ldconfig in scriptlets.
- Split systemd-analyze to a subpackage.

* Sat Jan 21 2012 Dan Horák <dan[at]danny.cz> - 38-4
- fix build on big-endians

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-3
- Disable building of gtk tools for now

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-2
- Fix a few (build) dependencies

* Wed Jan 11 2012 Lennart Poettering <lpoetter@redhat.com> - 38-1
- New upstream release

* Tue Nov 15 2011 Michal Schmidt <mschmidt@redhat.com> - 37-4
- Run authconfig if /etc/pam.d/system-auth is not a symlink.
- Resolves: #753160

* Wed Nov 02 2011 Michal Schmidt <mschmidt@redhat.com> - 37-3
- Fix remote-fs-pre.target and its ordering.
- Resolves: #749940

* Wed Oct 19 2011 Michal Schmidt <mschmidt@redhat.com> - 37-2
- A couple of fixes from upstream:
- Fix a regression in bash-completion reported in Bodhi.
- Fix a crash in isolating.
- Resolves: #717325

* Tue Oct 11 2011 Lennart Poettering <lpoetter@redhat.com> - 37-1
- New upstream release
- Resolves: #744726, #718464, #713567, #713707, #736756

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-5
- Undo the workaround. Kay says it does not belong in systemd.
- Unresolves: #741655

* Thu Sep 29 2011 Michal Schmidt <mschmidt@redhat.com> - 36-4
- Workaround for the crypto-on-lvm-on-crypto disk layout
- Resolves: #741655

* Sun Sep 25 2011 Michal Schmidt <mschmidt@redhat.com> - 36-3
- Revert an upstream patch that caused ordering cycles
- Resolves: #741078

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-2
- Add /etc/timezone to ghosted files

* Fri Sep 23 2011 Lennart Poettering <lpoetter@redhat.com> - 36-1
- New upstream release
- Resolves: #735013, #736360, #737047, #737509, #710487, #713384

* Thu Sep  1 2011 Lennart Poettering <lpoetter@redhat.com> - 35-1
- New upstream release
- Update post scripts
- Resolves: #726683, #713384, #698198, #722803, #727315, #729997, #733706, #734611

* Thu Aug 25 2011 Lennart Poettering <lpoetter@redhat.com> - 34-1
- New upstream release

* Fri Aug 19 2011 Harald Hoyer <harald@redhat.com> 33-2
- fix ABRT on service file reloading
- Resolves: rhbz#732020

* Wed Aug  3 2011 Lennart Poettering <lpoetter@redhat.com> - 33-1
- New upstream release

* Fri Jul 29 2011 Lennart Poettering <lpoetter@redhat.com> - 32-1
- New upstream release

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-2
- Fix access mode of modprobe file, restart logind after upgrade

* Wed Jul 27 2011 Lennart Poettering <lpoetter@redhat.com> - 31-1
- New upstream release

* Wed Jul 13 2011 Lennart Poettering <lpoetter@redhat.com> - 30-1
- New upstream release

* Thu Jun 16 2011 Lennart Poettering <lpoetter@redhat.com> - 29-1
- New upstream release

* Mon Jun 13 2011 Michal Schmidt <mschmidt@redhat.com> - 28-4
- Apply patches from current upstream.
- Fixes memory size detection on 32-bit with >4GB RAM (BZ712341)

* Wed Jun 08 2011 Michal Schmidt <mschmidt@redhat.com> - 28-3
- Apply patches from current upstream
- https://bugzilla.redhat.com/show_bug.cgi?id=709909
- https://bugzilla.redhat.com/show_bug.cgi?id=710839
- https://bugzilla.redhat.com/show_bug.cgi?id=711015

* Sat May 28 2011 Lennart Poettering <lpoetter@redhat.com> - 28-2
- Pull in nss-myhostname

* Thu May 26 2011 Lennart Poettering <lpoetter@redhat.com> - 28-1
- New upstream release

* Wed May 25 2011 Lennart Poettering <lpoetter@redhat.com> - 26-2
- Bugfix release
- https://bugzilla.redhat.com/show_bug.cgi?id=707507
- https://bugzilla.redhat.com/show_bug.cgi?id=707483
- https://bugzilla.redhat.com/show_bug.cgi?id=705427
- https://bugzilla.redhat.com/show_bug.cgi?id=707577

* Sat Apr 30 2011 Lennart Poettering <lpoetter@redhat.com> - 26-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=699394
- https://bugzilla.redhat.com/show_bug.cgi?id=698198
- https://bugzilla.redhat.com/show_bug.cgi?id=698674
- https://bugzilla.redhat.com/show_bug.cgi?id=699114
- https://bugzilla.redhat.com/show_bug.cgi?id=699128

* Thu Apr 21 2011 Lennart Poettering <lpoetter@redhat.com> - 25-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694788
- https://bugzilla.redhat.com/show_bug.cgi?id=694321
- https://bugzilla.redhat.com/show_bug.cgi?id=690253
- https://bugzilla.redhat.com/show_bug.cgi?id=688661
- https://bugzilla.redhat.com/show_bug.cgi?id=682662
- https://bugzilla.redhat.com/show_bug.cgi?id=678555
- https://bugzilla.redhat.com/show_bug.cgi?id=628004

* Wed Apr  6 2011 Lennart Poettering <lpoetter@redhat.com> - 24-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=694079
- https://bugzilla.redhat.com/show_bug.cgi?id=693289
- https://bugzilla.redhat.com/show_bug.cgi?id=693274
- https://bugzilla.redhat.com/show_bug.cgi?id=693161

* Tue Apr  5 2011 Lennart Poettering <lpoetter@redhat.com> - 23-1
- New upstream release
- Include systemd-sysv-convert

* Fri Apr  1 2011 Lennart Poettering <lpoetter@redhat.com> - 22-1
- New upstream release

* Wed Mar 30 2011 Lennart Poettering <lpoetter@redhat.com> - 21-2
- The quota services are now pulled in by mount points, hence no need to enable them explicitly

* Tue Mar 29 2011 Lennart Poettering <lpoetter@redhat.com> - 21-1
- New upstream release

* Mon Mar 28 2011 Matthias Clasen <mclasen@redhat.com> - 20-2
- Apply upstream patch to not send untranslated messages to plymouth

* Tue Mar  8 2011 Lennart Poettering <lpoetter@redhat.com> - 20-1
- New upstream release

* Tue Mar  1 2011 Lennart Poettering <lpoetter@redhat.com> - 19-1
- New upstream release

* Wed Feb 16 2011 Lennart Poettering <lpoetter@redhat.com> - 18-1
- New upstream release

* Mon Feb 14 2011 Bill Nottingham <notting@redhat.com> - 17-6
- bump upstart obsoletes (#676815)

* Wed Feb  9 2011 Tom Callaway <spot@fedoraproject.org> - 17-5
- add macros.systemd file for %%{_unitdir}

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Lennart Poettering <lpoetter@redhat.com> - 17-3
- Fix popen() of systemctl, #674916

* Mon Feb  7 2011 Bill Nottingham <notting@redhat.com> - 17-2
- add epoch to readahead obsolete

* Sat Jan 22 2011 Lennart Poettering <lpoetter@redhat.com> - 17-1
- New upstream release

* Tue Jan 18 2011 Lennart Poettering <lpoetter@redhat.com> - 16-2
- Drop console.conf again, since it is not shipped in pamtmp.conf

* Sat Jan  8 2011 Lennart Poettering <lpoetter@redhat.com> - 16-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 15-1
- New upstream release

* Thu Nov 25 2010 Lennart Poettering <lpoetter@redhat.com> - 14-1
- Upstream update
- Enable hwclock-load by default
- Obsolete readahead
- Enable /var/run and /var/lock on tmpfs

* Fri Nov 19 2010 Lennart Poettering <lpoetter@redhat.com> - 13-1
- new upstream release

* Wed Nov 17 2010 Bill Nottingham <notting@redhat.com> 12-3
- Fix clash

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-2
- Don't clash with initscripts for now, so that we don't break the builders

* Wed Nov 17 2010 Lennart Poettering <lpoetter@redhat.com> - 12-1
- New upstream release

* Fri Nov 12 2010 Matthias Clasen <mclasen@redhat.com> - 11-2
- Rebuild with newer vala, libnotify

* Thu Oct  7 2010 Lennart Poettering <lpoetter@redhat.com> - 11-1
- New upstream release

* Wed Sep 29 2010 Jesse Keating <jkeating@redhat.com> - 10-6
- Rebuilt for gcc bug 634757

* Thu Sep 23 2010 Bill Nottingham <notting@redhat.com> - 10-5
- merge -sysvinit into main package

* Mon Sep 20 2010 Bill Nottingham <notting@redhat.com> - 10-4
- obsolete upstart-sysvinit too

* Fri Sep 17 2010 Bill Nottingham <notting@redhat.com> - 10-3
- Drop upstart requires

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-2
- Enable audit
- https://bugzilla.redhat.com/show_bug.cgi?id=633771

* Tue Sep 14 2010 Lennart Poettering <lpoetter@redhat.com> - 10-1
- New upstream release
- https://bugzilla.redhat.com/show_bug.cgi?id=630401
- https://bugzilla.redhat.com/show_bug.cgi?id=630225
- https://bugzilla.redhat.com/show_bug.cgi?id=626966
- https://bugzilla.redhat.com/show_bug.cgi?id=623456

* Fri Sep  3 2010 Bill Nottingham <notting@redhat.com> - 9-3
- move fedora-specific units to initscripts; require newer version thereof

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-2
- Add missing tarball

* Fri Sep  3 2010 Lennart Poettering <lpoetter@redhat.com> - 9-1
- New upstream version
- Closes 501720, 614619, 621290, 626443, 626477, 627014, 627785, 628913

* Fri Aug 27 2010 Lennart Poettering <lpoetter@redhat.com> - 8-3
- Reexecute after installation, take ownership of /var/run/user
- https://bugzilla.redhat.com/show_bug.cgi?id=627457
- https://bugzilla.redhat.com/show_bug.cgi?id=627634

* Thu Aug 26 2010 Lennart Poettering <lpoetter@redhat.com> - 8-2
- Properly create default.target link

* Wed Aug 25 2010 Lennart Poettering <lpoetter@redhat.com> - 8-1
- New upstream release

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623561

* Thu Aug 12 2010 Lennart Poettering <lpoetter@redhat.com> - 7-2
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=623430

* Tue Aug 10 2010 Lennart Poettering <lpoetter@redhat.com> - 7-1
- New upstream release

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-2
- properly hide output on package installation
- pull in coreutils during package installtion

* Fri Aug  6 2010 Lennart Poettering <lpoetter@redhat.com> - 6-1
- New upstream release
- Fixes #621200

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-2
- Add tarball

* Wed Aug  4 2010 Lennart Poettering <lpoetter@redhat.com> - 5-1
- Prepare release 5

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 4-4
- Add 'sysvinit-userspace' provide to -sysvinit package to fix upgrade/install (#618537)

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-3
- Add libselinux to build dependencies

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-2
- Use the right tarball

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-1
- New upstream release, and make default

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-3
- Used wrong tarball

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-2
- Own /cgroup jointly with libcgroup, since we don't dpend on it anymore

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-1
- New upstream release

* Fri Jul 9 2010 Lennart Poettering <lpoetter@redhat.com> - 2-0
- New upstream release

* Wed Jul 7 2010 Lennart Poettering <lpoetter@redhat.com> - 1-0
- First upstream release

* Tue Jun 29 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.7.20100629git4176e5
- New snapshot
- Split off -units package where other packages can depend on without pulling in the whole of systemd

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.6.20100622gita3723b
- Add missing libtool dependency.

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.5.20100622gita3723b
- Update snapshot

* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Fri Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
