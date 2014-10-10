# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       ktexteditor

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 advanced embeddable text editor
Version:    5.3.0
Release:    2
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  ktexteditor.yaml
Source101:  ktexteditor-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  sonnet-devel

%description
KDE Frameworks 5 Tier 3 advanced embeddable text editor


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kparts-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%find_lang ktexteditor5_qt --with-qt --all-name || :

%files -f ktexteditor5_qt.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_sysconfdir}/xdg/kate*
%{_kf5_libdir}/libKF5TextEditor.so.*
%{_kf5_plugindir}/*
%{_kf5_servicesdir}/katepart.desktop
%{_kf5_servicetypesdir}/*.desktop
%{_kf5_sharedir}/katepart5/*
%{_kf5_sharedir}/kxmlgui5/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5TextEditor.so
%{_kf5_cmakedir}/KF5TextEditor
%{_kf5_includedir}/ktexteditor_version.h
%{_kf5_includedir}/KTextEditor
%{_kf5_mkspecsdir}/*.pri
# >> files devel
# << files devel
