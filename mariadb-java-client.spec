Name:           mariadb-java-client
Version:        1.3.2
Release:        1%{?dist}
Summary:        Connects applications developed in Java to MariaDB and MySQL databases

License:        LGPLv2+
URL:            https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:        https://downloads.mariadb.com/files/MariaDB/connector-java-%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  maven-local
Requires:       mariadb

%description
MariaDB Connector/J is a Type 4 JDBC driver, also known as the Direct to
Database Pure Java Driver. It was developed specifically as a lightweight
JDBC connector for use with MySQL and MariaDB database servers.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%build
%mvn_install


%install
%mvn_install


%files 




%changelog
* Mon Dec  7 2015 Tomáš Repík <trepik@redhat.com> - 1.3.2-1
- Initial package
