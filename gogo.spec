Summary:	MP3 encoder based on lame
Summary(pl):	Program do kompresji plików MP3 na podstawie lame
Name:		gogo
Version:	239b
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
URL:		http://homepage1.nifty.com/herumi/soft.html
Source0:	http://homepage1.nifty.com/herumi/soft/gogo2/src/%{name}%{version}.tgz
BuildRequires:	nasm
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software is based lame MP3 encoder. GOGO can encode about TWICE
as fast as original LAME can on K6-2 315MHz, and its quality is the
about same as LAME's. GOGO makes use of MMX, (Enhanced) 3D Now! and
SSE if your system supports these units.

%description -l pl
GOGO jest programem do kompresji plików MP3, który zosta³ stworzony na
podstawie programu lame. Program ten potrafi byæ dwa razy szybszy od
orygina³u w systemie z procesorem K6-2 315MHz, zachowuj±c jednocze¶nie
jako¶æ kompresowanych plików. GOGO wykorzystuje MMX, instrukcje 3D
Now! oraz SSE.

%prep
%setup -q -n %{name}%{version}

%build
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	USE_E3DN=yes
cd contrib
gcc -o cdda2mp3 cdda2mp3.c %{rpmcflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gogo contrib/cdda2mp3 $RPM_BUILD_ROOT%{_bindir}

gzip -9nf readme.txt japandoc/[fi]* contrib/cdda2mp3.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz contrib/*.gz japandoc/*.gz
%attr(755,root,root) %{_bindir}/*
