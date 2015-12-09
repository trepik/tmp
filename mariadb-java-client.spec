%global _mavenmetadir /usr/share/maven-metadata

Name:           mariadb-java-client
Version:        1.3.3
Release:        1%{?dist}
Summary:        Connects applications developed in Java to MariaDB and MySQL databases

License:        LGPLv2+
URL:            https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:        https://downloads.mariadb.com/files/MariaDB/connector-java-%{version}/%{name}-%{version}.tar.gz
# Source code available also @ https://github.com/MariaDB/mariadb-connector-j

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
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
%setup -cn %{name}-%{version}
# Cleanup
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# Fix BR
# net.java.dev.jna:jna:jar:platform:3.3.0
%pom_xpath_remove "pom:dependency[pom:classifier = 'platform']"
%pom_add_dep net.java.dev.jna:jna-platform:'${jna.version}'

%mvn_file org.mariadb.jdbc:%{name} %{name}
%mvn_alias org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%build
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc documentation/* README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Dec  9 2015 Tomáš Repík <trepik@redhat.com> - 1.3.3-1
- Initial package
