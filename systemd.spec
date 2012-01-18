Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Version:        37
Release:        8%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Summary:        A System and Service Manager
BuildRequires:  libudev-devel >= 160
BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libselinux-devel
BuildRequires:  audit-libs-devel
BuildRequires:  cryptsetup-luks-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  vala >= 0.11
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgee-devel
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  libacl-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  intltool >= 0.40.0
BuildRequires:  binutils
BuildRequires:  gperf
BuildRequires:  gawk
Requires(post): authconfig
Requires:       systemd-units = %{version}-%{release}
Requires:       dbus >= 1.4.6-3.fc15
Requires:       udev >= 167
Requires:       libudev >= 160
Requires:       initscripts >= 9.28
Requires:       filesystem >= 2.4.40
Conflicts:      selinux-policy < 3.9.16-12.fc15
Conflicts:      kernel < 2.6.35.2-9.fc14
Requires:       nss-myhostname
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2
# Adds support for the %%{_unitdir} macro
Source1:        macros.systemd
Source2:        systemd-sysv-convert
# Stop-gap, just to ensure things work out-of-the-box for this driver.
Source3:        udlfb.conf
# selected patches from v38
Patch0001:      0001-util-properly-detect-what-the-last-capability-is.patch
Patch0002:      0002-manager-fix-a-crash-in-isolating.patch
Patch0003:      0003-audit-do-not-complain-if-kernel-lacks-audit.patch
Patch0004:      0004-systemctl-completion-always-invoke-with-no-legend.patch
Patch0005:      0005-systemctl-make-list-unit-files-output-more-economica.patch
Patch0006:      0006-plymouth-fix-ply-proto-endianess-issues.patch
Patch0007:      0007-random-seed-convert-poolsize-from-bits-to-bytes.patch
Patch0008:      0008-condition-Fix-file-descriptor-leak-in-test_capabilit.patch
Patch0009:      0009-initctl-don-t-use-dbus-connection-after-PID-1-got-re.patch
Patch0010:      0010-cgroup-always-recreate-cgroup-before-we-try-to-apply.patch
Patch0011:      0011-mount-order-remote-mounts-after-both-network.target-.patch
Patch0012:      0012-units-drop-Install-section-from-remote-fs-pre.target.patch
Patch0013:      0013-cryptsetup-generator-avoid-ordering-cycle-on-swap.patch
Patch0014:      0014-bash-completion-update-with-new-verbs-and-arguments.patch
Patch0015:      0015-bash-completion-add-completions-for-systemd-loginctl.patch
Patch0016:      0016-bash-completion-rename-file-since-it-is-no-longer-fo.patch
Patch0017:      0017-systemadm-break-timestamp-formatting-out-into-a-sepe.patch
Patch0018:      0018-systemadm-allow-sorting-of-jobs-and-units.patch
Patch0019:      0019-systemadm-split-the-type-status-combo-box-into-type-.patch
Patch0020:      0020-systemadm-filter-on-swaps-paths-and-timers-too.patch
Patch0021:      0021-systemadm-add-a-wrappable-label-and-use-it-for-statu.patch
Patch0022:      0022-systemadm-add-libgee-as-dependency-and-use-it-for-a-.patch
Patch0023:      0023-systemadm-display-dependencies-sorted.patch
Patch0024:      0024-systemadm-use-color-for-dependency-links.patch
Patch0025:      0025-systemadm-use-bold-for-requires-etc.patch
Patch0026:      0026-systemadm-make-the-dependency-listing-selectable.patch
Patch0027:      0027-systemadm-catch-exceptions-generated-by-dbus.patch
Patch0028:      0028-systemadm-coalesce-id-and-decription-fields.patch
Patch0029:      0029-systemadm-adjust-row-numbers-after-removing-aliases.patch
Patch0030:      0030-systemadm-use-colors-for-id-too-remove-color-from-fr.patch
Patch0031:      0031-cgroup-immediately-remove-all-cgroups-which-run-empt.patch
Patch0032:      0032-utmp-remove-unneded-parameters.patch
Patch0033:      0033-utmp-no-need-to-zero-a-struct-before-overwriting-it-.patch
Patch0034:      0034-utmp-initialize-store-with-the-found-entry-not-with-.patch
Patch0035:      0035-utmp-for-DEAD_PROCESS-write-the-current-time-to-wtmp.patch
Patch0036:      0036-man-fix-a-typo-in-signal-number.patch
Patch0037:      0037-units-drop-unnecessary-StandardOutput-syslog.patch
Patch0038:      0038-units-fedora-let-rc-local.service-log-to-syslog.patch
Patch0039:      0039-service-don-t-warn-if-the-pidfile-still-exists-after.patch
Patch0040:      0040-job-colored-status-messages-on-boot.patch
Patch0041:      0041-man-fix-typo-in-sd_notify.patch
Patch0042:      0042-Fix-same-expression-on-both-sides-of.patch
Patch0043:      0043-execute-avoid-logging-to-closed-fds.patch
Patch0044:      0044-execute-make-setup_pam-return-errno-when-possible.patch
Patch0045:      0045-execute-log-errors-from-sd-EXEC.patch
Patch0046:      0046-pam-module-use-the-correct-session-type-unspecified.patch
Patch0047:      0047-pam-module-treat-cron-in-PAM_TTY-as-empty-tty.patch
Patch0048:      0048-let-mount-and-swap-units-log-to-the-configured-defau.patch
Patch0049:      0049-socket-add-option-for-SO_PASSCRED.patch
Patch0050:      0050-shutdownd-use-PassCred-yes-in-the-socket-unit.patch
Patch0051:      0051-syslog-use-PassCred-yes-for-the-dev-log-socket.patch
Patch0052:      0052-man-document-the-PassCred-option.patch
Patch0053:      0053-add-a-generator-to-pull-rc-local.service-in.patch
Patch0054:      0054-rc-local-no-need-to-check-if-the-script-is-executabl.patch
Patch0055:      0055-rc-local-order-after-network.target.patch
Patch0056:      0056-util-fix-error-checking-after-fgets.patch
Patch0057:      0057-path-use-m-instead-of-strerror-errno.patch
Patch0058:      0058-path-refactor-PathSpec-usage.patch
Patch0059:      0059-path-add-PathModified-PathChanged-IN_MODIFY.patch
Patch0060:      0060-service-handle-services-with-racy-daemonization-grac.patch
Patch0061:      0061-service-stop-the-service-if-ExecStartPost-ends-with-.patch
Patch0062:      0062-Allow-list-unit-files-to-run-with-root.patch
Patch0063:      0063-unit-garbage-collect-units-with-load-error.patch
Patch0064:      0064-systemctl-print-error-load-state-in-red.patch
Patch0065:      0065-is-an-ampersat-not-an-ampersand-let-s-call-it-at-sym.patch
Patch0066:      0066-path-add-missing-pieces-for-PathModified.patch
Patch0067:      0067-unit-fix-false-positive-in-check-for-unneeded-unit.patch
Patch0068:      0068-unit-check-for-unneeded-dependencies-even-when-unit-.patch
Patch0069:      0069-pam-module-add-a-couple-of-debugging-prints.patch
Patch0070:      0070-fsck-Fix-typo-in-comment.patch
Patch0071:      0071-systemctl-fix-typo-in-is-enabled.patch
Patch0072:      0072-tmpfiles-use-an-enum-instead-of-plain-char-for-item-.patch
Patch0073:      0073-tmpfiles-rename-a-couple-of-functions.patch
Patch0074:      0074-tmpfiles-use-a-common-function-to-set-owner-group-mo.patch
Patch0075:      0075-tmpfiles-separate-a-generic-item-glob-processing-fun.patch
Patch0076:      0076-tmpfiles-add-RECURSIVE_RELABEL_PATH-Z.patch
Patch0077:      0077-man-document-Z-in-tmpfiles.patch
Patch0078:      0078-man-mention-that-Z-ignores-uid-gid-mode.patch
Patch0079:      0079-service-use-syslog-console-for-sysv_console.patch
Patch0080:      0080-tmpfiles-apply-chown-chmod-for-Z-entries-too.patch
Patch0081:      0081-tmpfiles-add-z-like-Z-but-not-recursive.patch
Patch0082:      0082-man-fix-misplaced-remark-in-description-of-Sockets.patch
Patch0083:      0083-execute-fix-losing-of-start-timestamps.patch
Patch0084:      0084-label-fix-labeling-of-symbolic-links.patch
Patch0085:      0085-dbus-register-to-DBus-asynchronously.patch
Patch0086:      0086-dbus-no-sync-D-Bus-connection-flushing.patch
Patch0087:      0087-log-never-block-on-syslog-in-PID-1.patch
Patch0088:      0088-macro-fix-ALIGN_TO-macro-definition.patch
Patch0089:      0089-man-document-the-sd-login-interfaces.patch
Patch0090:      0090-sd-daemon-fix-include-lines-since-we-now-ship-a-shar.patch
Patch0091:      0091-man-build-new-man-pages.patch
Patch0092:      0092-man-sd_readahead-is-not-actually-available-in-libsys.patch
Patch0093:      0093-build-sys-add-rules-for-man-page-aliases.patch
Patch0094:      0094-man-add-sd-login-7-page.patch
Patch0095:      0095-man-various-updates.patch
Patch0096:      0096-man-extend-sd-login-7-in-regards-to-mixing-D-Bus-and.patch
Patch0097:      0097-man-generate-HTML-instead-of-XHTML-with-XSL-docbook-.patch
Patch0098:      0098-man-switch-to-UTF-8-output-to-work-around-charset-is.patch
Patch0099:      0099-udev-exclude-loopback-device-from-udev-rule-based-sy.patch
Patch0100:      0100-remount-api-vfs-handle-another-OOM-condition.patch
Patch0101:      0101-socket-rename-the-PassCred-option-to-PassCredentials.patch
Patch0102:      0102-socket-only-add-dependency-on-kmsg-socket-to-socket-.patch
Patch0103:      0103-readahead-bring-export-definition-of-sd-readahead-in.patch
Patch0104:      0104-nspawn-get-rid-of-BUFFER_SIZE-use-LINE_MAX-instead.patch
Patch0105:      0105-namespace-remount-namespace-root-dir-for-SLAVE-to-av.patch
Patch0106:      0106-logind-if-we-can-t-open-dev-tty0-assume-there-is-no-.patch
Patch0107:      0107-logind-don-t-watch-vcsa-if-nobody-cares.patch
Patch0108:      0108-man-fix-SEE-ALSO-in-hostname-5.patch
Patch0109:      0109-logind-send-out-Lock-signal-when-locking.patch
Patch0110:      0110-logind-add-needed-include-for-sd_notify.patch
Patch0111:      0111-fix-compilation-error-with-PathSpec-redefined.patch
Patch0112:      0112-util-when-printing-status-updates-during-boot-take-t.patch
Patch0113:      0113-log-minor-optimization.patch
Patch0114:      0114-util-never-ellipsize-welcome-message.patch
Patch0115:      0115-headers-fix-git-URLs-for-source-files.patch
Patch0116:      0116-README-correct-license-claims.patch
Patch0117:      0117-util-fix-switching-to-console-unicode-mode.patch
Patch0118:      0118-util-switch-the-console-to-text-mode-on-reset.patch
Patch0119:      0119-service-add-dependencies-on-configured-sockets.patch
Patch0120:      0120-unit-properly-update-references-to-units-which-are-m.patch
Patch0121:      0121-main-fix-spelling.patch
Patch0122:      0122-load-fragment-fix-parsing-of-Socket-setting.patch
Patch0123:      0123-fix-compiler-warning.patch
Patch0124:      0124-shutdown-exclude-processes-with-argv-0-0-from-killin.patch
Patch0125:      0125-shutdown-add-link-to-root-storage-daemon-text.patch
Patch0126:      0126-unit-implement-new-PropagateReloadTo-PropagateReload.patch
# from v39:
Patch0127:      0127-tmpfiles-fix-parsing-of-proc-net-unix-on-32Bit-machi.patch
Patch0128:      0128-pam-work-correctly-if-a-seat-is-specified-but-not-vt.patch
Patch0129:      0129-pam-fix-build.patch
Patch0130:      0130-mount-fix-quota.patch
Patch0131:      0131-logind-downgrade-login-message-to-debug.patch

# For sysvinit tools
Obsoletes:      SysVinit < 2.86-24, sysvinit < 2.86-24
Provides:       SysVinit = 2.86-24, sysvinit = 2.86-24
Provides:       sysvinit-userspace
Provides:       systemd-sysvinit
Obsoletes:      systemd-sysvinit
Obsoletes:      upstart < 1.2-3
Obsoletes:      upstart-sysvinit < 1.2-3
Conflicts:      upstart-sysvinit
Obsoletes:      readahead < 1:1.5.7-3
Provides:       readahead = 1:1.5.7-3

%description
systemd is a system and service manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package units
Group:          System Environment/Base
Summary:        Configuration files, directories and installation tool for systemd
Requires:       pkgconfig
Requires(post): coreutils
Requires(post): gawk

%description units
Basic configuration files, directories and installation tool for the systemd
system and service manager.

%package devel
Group:          System Environment/Base
Summary:        Development headers for systemd
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development headers and auxiliary files for developing applications for systemd.

%package gtk
Group:          System Environment/Base
Summary:        Graphical frontend for systemd
Requires:       %{name} = %{version}-%{release}
Requires:       polkit

%description gtk
Graphical front-end for systemd.

%package sysv
Group:          System Environment/Base
Summary:        SysV tools for systemd
Requires:       %{name} = %{version}-%{release}

%description sysv
SysV compatibility tools for systemd

%prep
%setup -q
set +x
for p in %{patches}; do
	echo "Applying $p"
	patch -p1 < $p
done
set -x

%build
autoreconf -i
%configure --with-rootdir= --with-distro=fedora --with-rootlibdir=/%{_lib}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/sbin
ln -s ../bin/systemd %{buildroot}/sbin/init
ln -s ../bin/systemctl %{buildroot}/sbin/reboot
ln -s ../bin/systemctl %{buildroot}/sbin/halt
ln -s ../bin/systemctl %{buildroot}/sbin/poweroff
ln -s ../bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../bin/systemctl %{buildroot}/sbin/telinit
ln -s ../bin/systemctl %{buildroot}/sbin/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}/etc/systemd/system/*.target.wants

# Make sure the ghost-ing below works
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel2.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel3.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel4.target
touch %{buildroot}%{_sysconfdir}/systemd/system/runlevel5.target

# Make sure these directories are properly owned
mkdir -p %{buildroot}/lib/systemd/system/basic.target.wants
mkdir -p %{buildroot}/lib/systemd/system/default.target.wants
mkdir -p %{buildroot}/lib/systemd/system/dbus.target.wants
mkdir -p %{buildroot}/lib/systemd/system/syslog.target.wants

# Create new-style configuration files so that we can ghost-own them
touch %{buildroot}%{_sysconfdir}/hostname
touch %{buildroot}%{_sysconfdir}/vconsole.conf
touch %{buildroot}%{_sysconfdir}/locale.conf
touch %{buildroot}%{_sysconfdir}/os-release
touch %{buildroot}%{_sysconfdir}/machine-id
touch %{buildroot}%{_sysconfdir}/machine-info
touch %{buildroot}%{_sysconfdir}/timezone
mkdir -p %{buildroot}%{_sysconfdir}/X11/xorg.conf.d
touch %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf

# Install RPM macros file for systemd
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/

# Install SysV conversion tool for systemd
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/

# Install modprobe fragment
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/modprobe.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/systemd-machine-id-setup > /dev/null 2>&1 || :
/bin/systemctl daemon-reexec > /dev/null 2>&1 || :

# Make sure pam_systemd is enabled
if ! /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac >/dev/null 2>&1 || ! [ -h /etc/pam.d/system-auth ] ; then
        /usr/sbin/authconfig --update --nostart >/dev/null 2>&1 || :

        # Try harder
        /bin/grep -q pam_systemd /etc/pam.d/system-auth-ac >/dev/null 2>&1 || /usr/sbin/authconfig --updateall --nostart >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ] ; then
        /bin/systemctl try-restart systemd-logind.service >/dev/null 2>&1 || :
fi

%post units
if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/lib/systemd/system/graphical.target"
        else
                target="/lib/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" /etc/systemd/system/default.target >/dev/null 2>&1 || :

        # Enable the services we install by default.
        /bin/systemctl enable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :
else
        # This systemd service does not exist anymore, we now do it
        # internally in PID 1
        /bin/rm -f /etc/systemd/system/sysinit.target.wants/hwclock-load.service >/dev/null 2>&1 || :
fi

%preun units
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                remote-fs.target \
                systemd-readahead-replay.service \
                systemd-readahead-collect.service >/dev/null 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target >/dev/null 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.hostname1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.login1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.locale1.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.timedate1.conf
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/user.conf
%config(noreplace) %{_sysconfdir}/systemd/systemd-logind.conf
%{_sysconfdir}/xdg/systemd
%{_libdir}/../lib/tmpfiles.d/systemd.conf
%{_libdir}/../lib/tmpfiles.d/x11.conf
%{_libdir}/../lib/tmpfiles.d/legacy.conf
%{_libdir}/../lib/tmpfiles.d/tmp.conf
%ghost %config(noreplace) %{_sysconfdir}/hostname
%ghost %config(noreplace) %{_sysconfdir}/vconsole.conf
%ghost %config(noreplace) %{_sysconfdir}/locale.conf
%ghost %config(noreplace) %{_sysconfdir}/os-release
%ghost %config(noreplace) %{_sysconfdir}/machine-id
%ghost %config(noreplace) %{_sysconfdir}/machine-info
%ghost %config(noreplace) %{_sysconfdir}/timezone
%ghost %config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/00-keyboard.conf
/bin/systemd
/bin/systemd-notify
/bin/systemd-ask-password
/bin/systemd-tty-ask-password-agent
/bin/systemd-machine-id-setup
/bin/systemd-loginctl
/usr/bin/systemd-nspawn
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-analyze
/lib/systemd/systemd-*
/lib/udev/rules.d/*.rules
/lib/systemd/system-generators/systemd-cryptsetup-generator
/lib/systemd/system-generators/systemd-getty-generator
/lib/systemd/system-generators/systemd-rc-local-generator
/%{_lib}/security/pam_systemd.so
/%{_lib}/libsystemd-daemon.so.*
/%{_lib}/libsystemd-login.so.*
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%{_bindir}/systemd-cgls
%{_mandir}/man1/*
%exclude %{_mandir}/man1/systemctl.*
%exclude %{_mandir}/man1/systemadm.*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_libdir}/../lib/systemd
%{_datadir}/systemd/kbd-model-map
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.hostname1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.login1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.locale1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.timedate1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.hostname1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.locale1.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.timedate1.xml
%{_docdir}/systemd
%{_datadir}/polkit-1/actions/org.freedesktop.systemd1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.hostname1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.login1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.locale1.policy
%{_datadir}/polkit-1/actions/org.freedesktop.timedate1.policy
%config(noreplace) %{_sysconfdir}/modprobe.d/udlfb.conf

%files units
%defattr(-,root,root,-)
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%dir %{_sysconfdir}/systemd/user
%dir %{_sysconfdir}/tmpfiles.d
%dir %{_sysconfdir}/sysctl.d
%dir %{_sysconfdir}/modules-load.d
%dir %{_sysconfdir}/binfmt.d
%dir %{_sysconfdir}/bash_completion.d
%dir /lib/systemd
%dir /lib/systemd/system-generators
%dir /lib/systemd/system-shutdown
%dir %{_libdir}/../lib/tmpfiles.d
%dir %{_libdir}/../lib/sysctl.d
%dir %{_libdir}/../lib/modules-load.d
%dir %{_libdir}/../lib/binfmt.d
/lib/systemd/system
/bin/systemctl
/bin/systemd-tmpfiles
%{_sysconfdir}/bash_completion.d/systemd-bash-completion.sh
%{_sysconfdir}/rpm/macros.systemd
%{_mandir}/man1/systemctl.*
%{_datadir}/pkgconfig/systemd.pc
%{_docdir}/systemd/LICENSE

# Make sure we don't remove runlevel targets from F14 alpha installs,
# but make sure we don't create then anew.
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%ghost %config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target

%files gtk
%defattr(-,root,root,-)
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsystemd-daemon.so
%{_libdir}/libsystemd-login.so
%{_includedir}/systemd/sd-login.h
%{_includedir}/systemd/sd-daemon.h
%{_libdir}/pkgconfig/libsystemd-daemon.pc
%{_libdir}/pkgconfig/libsystemd-login.pc

%files sysv
%defattr(-,root,root,-)
%{_bindir}/systemd-sysv-convert

%changelog
* Tue Jan 17 2012 Michal Schmidt <mschmidt@redhat.com> - 37-8
- Shut up another logind message (#727315).

* Sat Jan 14 2012 Michal Schmidt <mschmidt@redhat.com> - 37-7
- Fix for quota and a couple of other issues.

* Wed Jan 11 2012 Michal Schmidt <mschmidt@redhat.com> - 37-6
- Fixes and low-risk enhancements (no journald) from upstream v38.

* Thu Dec 02 2011 Karsten Hopp <karsten@redhat.com> - 37-5
- add upstream patch for bugzilla 744415, encrypted filesystem passphrases 
  fail on runtime systems in hvc consoles

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

* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
