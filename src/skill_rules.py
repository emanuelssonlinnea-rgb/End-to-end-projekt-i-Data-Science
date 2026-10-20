# TIER 1 - PHRASES, matched in ANY case
# Taxonomy labels, copied as-is.

TIER1_PHRASES = [
    "Kravhantering",
    "Systemanalys",  # New
    "Systemarkitektur",  # New
    "Systemintegration",  # New
    "Verksamhetsutveckling",  # New
    "Cybersäkerhet",  # New
    "Oracle SOA Suite",  # New
    "Docker",
    "IBM Cloud",
    "Sun Java Enterprise System",
    "Windows Server",
    "Associate Android Developer",
    "Oracle Certified Associate",
    "PHP Developer Certification",
    "AWS Certified Solutions Architect",  # New
    "Clojure",
    "ClojureScript",
    "CoffeeScript",
    "Datalog",
    "Elixir",
    "OCaml",
    "OpenEdge Advanced Business Language",
    "PowerScript",
    "TypeScript",
    "Vyper",
    "XQuery",
    "Python",  # New
    "Java",  # New
    "JavaScript",  # New
    "MATLAB",  # New
    "Bash",  # New
    "SQL",  # New
    "GraphQL",  # New
    "Citrix",
    "IBM MQ",
    "TIBCO",
    "Oracle Fusion Middleware",
    "Software AG Integration Suite",
    "Databricks",  # New
    "Informatica",  # New
    "TCP/IP",
    "Bower",
    "Grunt",
    "Vagrant",
    "Jenkins",
    "Azure DevOps",
    "ASP.NET Core",
    "ASP.NET MVC",
    "Eclipselink",
    "Hibernate",
    "spaCy",
    "TensorFlow",
    "FastAPI",
    "OpenJPA",
    "Toplink",
    "Amazon Linux",  # New
    "Android",
    "Arch Linux",  # New
    "BlackBerry",
    "FreeBSD",  # New
    "Gentoo Linux",  # New
    "Kali Linux",  # New
    "Mac OS X",
    "NetBSD",  # New
    "openEuler",  # New
    "Oracle Linux",  # New
    "OS/390",
    "OS/400",
    "Raspberry Pi OS",  # New
    "Red Hat Enterprise Linux (RHEL)",  # New
    "Rocky Linux",  # New
    "Solaris",
    "Ubuntu",
    "VxWorks",
    "Windows för mobila enheter",
    "Windows",
    "Agile",  # New
    "API-design",
    "Artificial Intelligence / Artificiell intelligens / AI",
    "Asset Information Management",
    "Automationsteknik",
    "Blockkedjeteknik",
    "Budgetansvar",
    "CASE-verktyg",
    "Configuration Management / CM",
    "CORBA, distribuerad objektteknik",
    "Databasdesign",
    "Datamodellering",
    "Dataskyddsförordningen / GDPR, erfarenhet",
    "Datawarehouse",
    "Design Thinking",
    "Digitalisering",  # New
    "Distribuerad objektteknik",
    "Dokumentation",  # New
    "Driva workshops",  # New
    "Engelska",  # New
    "ERP-system, erfarenhet",
    "Felsökningsverktyg",
    "Förändringsledning",
    "Geografiskt informationssystem / GIS",
    "Git",  # New
    "Grafiska gränssnitt / GUI",
    "IANA/ICANN, bestämmelser och rekommendationer",
    "Informatik",
    "Informationsarkitektur",
    "Informationsmodellering",
    "Informationsstrategi",
    "Interaktionsdesign",
    "IT-konsultuppdrag, erfarenhet",
    "Kanban",
    "Kvalitetskontrollsystem, erfarenhet",
    "Länkad data",
    "Ledning",  # New
    "Machine learning / Maskininlärning",
    "Människa-datorinteraktion / MDI",
    "Masterdata",
    "Medieteknik",
    "Model-view-viewmodel (MVVM)",
    "Molnteknik",
    "Objektorienterad metodik",
    "Parallell programmering",
    "pm3, förvaltningsmodell",
    "Praktisk ProjektStyrning / PPS",
    "Prediktiv analys",
    "Projektledning, IT",
    "PROPS, projektstyrningsmodell",
    "Säkerhetsanalys, datasäkerhet",
    "Scaled Agile Framework / SAFe",
    "Svenska",  # New
    "Systemförvaltning",
    "Systemintegrering",
    "Systemutredning",
    "Telematik",
    "Testautomatisering / Test automation",
    "Tjänsteorienterande arkitektur / SOA",
    "Verksamhetsanalys",
    "WAP-teknik",
    "Web Accessibility Initiative / WAI",
    "Web Content Accessibility Guidelines / WCAG",
    "Webbutveckling",
]


# TIER 2 - EXACT CASE, short or ambiguous words
# {canonical skill: [exact spellings]}

TIER2_EXACT_CASE = {
    "A+": ["A+"],
    "Odoo": ["Odoo"],
    "SAP": ["SAP"],
    "R": ["R"],
    "Dart": ["Dart"],
    "Julia": ["Julia"],  # New
    "Scala": ["Scala"],  # New
    "SAS": ["SAS"],  # New
    "Cypher": ["Cypher"],  # New
    "C++": ["C++"],  # New
    "LDAP": ["LDAP"],
    "LINQ": ["LINQ"],
    "MDX": ["MDX"],
    "N1QL": ["N1QL"],
    "SPARQL": ["SPARQL"],
    "DAX": ["DAX"],  # New
    "dbt": ["dbt"],  # New
    "SOAP": ["SOAP"],
    # "DM": ["DM"],
    "Ethics": ["ETHICS"],
    "ISAC": ["ISAC"],
    "OOS": ["OOS"],
    "SOLID": ["SOLID"],
    "LSE": ["LSE"],
    "Logic": ["Logic"],
    "SVEA": ["SVEA"],
    "AIX": ["AIX"],  # New
    "CentOS": ["CentOS"],  # New
    "DOS": ["DOS"],
    "GNU": ["GNU"],
    "iOS": ["iOS"],
    "IRIX": ["IRIX"],
    "JCL": ["JCL"],
    "Linux": ["Linux"],
    "MVS": ["MVS"],
    "NixOS": ["NixOS"],  # New
    "OSE": ["OSE"],
    "pSOS": ["pSOS"],
    "UNIX": ["UNIX"],
    "VM/CMS": ["VM/CMS"],
    "VMS": ["VMS"],
    "VSE": ["VSE"],
    "OSL": ["OSL"],
}


# TIER 3 - CUSTOM ALIASES
# {canonical skill: {"any_case": [...], "exact_case": [...]}}

TIER3_CUSTOM = {
    "Internet Information Services": {
        "any_case": [
            "Internet Information Services",
            "Internet Information Services (IIS)",
        ],
        "exact_case": ["IIS"],
    },
    "Oracle Cloud Infrastructure": {
        "any_case": [
            "Oracle Cloud Infrastructure",
            "Oracle Cloud Infrastructure (OCI)",
            "Oracle Cloud",
        ],
        "exact_case": ["OCI"],
    },  # New
    "Amazon Web Services": {
        "any_case": ["Amazon Web Services", "Amazon Web Services (AWS)"],
        "exact_case": ["AWS"],
    },
    "Infor": {
        "any_case": ["Infor OS", "Infor CloudSuite"],
        "exact_case": ["Infor"],
    },
    "Microsoft Dynamics 365": {
        "any_case": ["Microsoft Dynamics 365", "Dynamics 365"],
        "exact_case": ["D365"],
    },
    "Office SharePoint Server": {
        "any_case": [
            "Office SharePoint Server",
            "Office SharePoint Server (MOSS)",
            "SharePoint Server",
            "SharePoint",
            "SharePoint Online",
        ],
        "exact_case": ["MOSS"],
    },
    "Oracle JCAPS": {
        "any_case": [
            "Oracle JCAPS",
            "Oracle Java CAPS",
            "Java Composite Application Platform Suite",
        ],
        "exact_case": ["Java CAPS"],
    },  # this was discontinued in 2016
    "Oracle Service Bus": {
        "any_case": ["Oracle Service Bus", "Oracle Service Bus (OSB)"],
        "exact_case": ["OSB"],
    },  # New
    "Oracle NetSuite": {
        "any_case": ["Oracle NetSuite", "NetSuite"],
    },
    "Salesforce Cloud": {
        "any_case": ["Salesforce Cloud", "Service Cloud", "Sales Cloud", "Salesforce"],
    },
    "MuleSoft Anypoint Platform": {
        "any_case": ["MuleSoft Anypoint Platform", "Mulesoft-plattformen", "MuleSoft"],
    },  # New
    "Red Hat OpenShift": {
        "any_case": ["Red Hat OpenShift", "OpenShift"],
    },  # New
    "AZ-204: Developing Solutions for Microsoft Azure": {
        "any_case": [
            "AZ-204: Developing Solutions for Microsoft Azure",
            "Developing Solutions for Microsoft Azure",
        ],
        "exact_case": ["AZ-204"],
    },
    "AZ-900: Microsoft Azure Fundamentals": {
        "any_case": [
            "AZ-900: Microsoft Azure Fundamentals",
            "Microsoft Azure Fundamentals",
        ],
        "exact_case": ["AZ-900"],
    },
    "MB-600: Microsoft Dynamics 365 Power Platform Solution Architect": {
        "any_case": [
            "MB-600: Microsoft Dynamics 365 Power Platform Solution Architect",
            "Dynamics 365 + Power Platform Solution Architect Expert",
        ],
        "exact_case": ["MB-600"],
    },
    "Microsoft 365 Certified: Fundamentals": {
        "any_case": [
            "Microsoft 365 Certified: Fundamentals",
            "Microsoft Certified: Fundamentals",
        ],
        "exact_case": ["MS-900"],
    },
    "Microsoft Certified: Application Developer": {
        "any_case": [
            "Microsoft Certified: Application Developer",
            "Microsoft Certified: Application Developer (MCAD)",
        ],
        "exact_case": ["MCAD"],
    },
    "Microsoft Certified: Database Administrator": {
        "any_case": [
            "Microsoft Certified: Database Administrator",
            "Microsoft Certified: Database Administrator (MCDBA)",
        ],
        "exact_case": ["MCDBA"],
    },
    "Microsoft Certified: Professional": {
        "any_case": [
            "Microsoft Certified: Professional",
            "Microsoft Certified: Professional (MCP)",
        ],
    },
    "Microsoft Certified: Solution Developer": {
        "any_case": [
            "Microsoft Certified: Solution Developer",
            "Microsoft Certified: Solution Developer (MCSD)",
        ],
        "exact_case": ["MCSD"],
    },
    "Microsoft Certified: System Engineer": {
        "any_case": [
            "Microsoft Certified: System Engineer",
            "Microsoft Certified: System Engineer (MCSE)",
        ],
        "exact_case": ["MCSE"],
    },
    "Microsoft Certified: Azure Administrator Associate": {
        "any_case": ["Microsoft Certified: Azure Administrator Associate"],
    },
    "Microsoft Certified: Azure Solutions Architect Expert": {
        "any_case": [
            "Microsoft Certified: Azure Solutions Architect Expert",
            "Azure Solutions Architect Expert",
        ],
    },  # New
    "Oracle Certified Database Administrator": {
        "any_case": [
            "Oracle Certified Database Administrator",
            "Oracle Certified Database Administrator (OCDBA)",
        ],
        "exact_case": ["OCDBA"],
    },
    "Oracle Certified Database Operator": {
        "any_case": [
            "Oracle Certified Database Operator",
            "Oracle Certified Database Operator (DBO)",
        ],
        "exact_case": ["DBO"],
    },
    "Oracle Certified Professional": {
        "any_case": [
            "Oracle Certified Professional",
            "Oracle Certified Professional/OCP",
            "Oracle Certified Professional (OCP)",
        ],
    },
    "Certified Business Analysis Professional": {
        "any_case": [
            "Certified Business Analysis Professional",
            "Certified Business Analysis Professional (CBAP)",
        ],
        "exact_case": ["CBAP"],
    },  # New
    "Entry Certificate in Business Analysis": {
        "any_case": [
            "Entry Certificate in Business Analysis",
            "Entry Certificate in Business Analysis (ECBA)",
        ],
        "exact_case": ["ECBA"],
    },  # New
    "TOGAF-certifiering": {
        "any_case": ["TOGAF-certifiering"],
        "exact_case": ["TOGAF"],
    },  # New
    "Certified JavaScript Developer": {
        "any_case": [
            "Certified JavaScript Developer",
            "JavaScript Developer-certifiering",
        ],
    },  # New
    "Windows Azure": {
        "any_case": ["Microsoft Azure", "Windows Azure"],
    },
    "Google Cloud Platform": {
        "any_case": ["Google Cloud", "Google Cloud Platform"],
        "exact_case": ["GCP"],
    },
    "Kubernetes": {"any_case": ["Kubernetes"], "exact_case": ["K8s"]},  # New
    "Apache Kafka": {
        "any_case": ["Apache Kafka", "Kafka"],
    },
    "Apache Tomcat": {
        "any_case": ["Apache Tomcat", "Tomcat"],
    },
    "Weblogic Server": {
        "any_case": ["Weblogic Server", "WebLogic", "Oracle WebLogic"],
    },
    "JBoss Application Server": {
        "any_case": ["JBoss Application Server", "JBoss", "JBoss EAP"],
    },
    "IBM WebSphere": {
        "any_case": ["IBM WebSphere", "WebSphere"],
    },
    "Glassfish Server": {
        "any_case": ["Glassfish Server", "GlassFish"],
    },
    "IBM Domino": {
        "any_case": ["IBM Domino", "HCL Domino", "Lotus Domino"],
    },
    "Java Server Pages (JSP)": {
        "any_case": ["Java Server Pages", "JavaServer Pages"],
        "exact_case": ["JSP"],
    },
    "IBM Integration Bus": {
        "any_case": ["IBM Integration Bus"],
        "exact_case": ["IIB"],
    },
    "JBoss Enterprise Middleware Suite (JEMS)": {
        "any_case": ["JBoss Enterprise Middleware Suite"],
        "exact_case": ["JEMS"],
    },
    "Microsoft BizTalk": {
        "any_case": ["Microsoft BizTalk", "BizTalk"],
    },
    "Oracle Data Integrator": {
        "any_case": ["Oracle Data Integrator"],
        "exact_case": ["ODI"],
    },
    "Software AG webMethods": {
        "any_case": ["Software AG webMethods", "webMethods"],
    },
    "Apache Airflow": {  # New
        "any_case": ["Apache Airflow"],
        "exact_case": ["Airflow"],
    },
    "Azure Data Factory": {  # New
        "any_case": ["Azure Data Factory"],
        "exact_case": ["ADF"],
    },
    "Apache Spark": {  # New
        "any_case": ["Apache Spark", "PySpark"],
        "exact_case": ["Spark"],
    },
    "Apache NiFi": {  # New
        "any_case": ["Apache NiFi", "NiFi"],
    },
    "Power Automate": {  # New
        "any_case": ["Power Automate", "Microsoft Power Automate"],
    },
    "Bluetooth-teknik": {
        "any_case": ["Bluetooth-teknik", "Bluetooth"],
        "exact_case": ["BLE"],
    },
    "HTTP/HTTPS": {
        "exact_case": ["HTTP", "HTTPS", "HTTP/HTTPS"],  # endast exakt skiftläge
    },
    "IP-telefoniteknik": {
        "any_case": ["IP-telefoniteknik", "IP-telefoni", "VoIP"],
    },
    "IR-teknik": {
        "any_case": ["IR-teknik", "infraröd teknik"],
    },
    "Local Interconnect Network (LIN)": {
        "any_case": ["Local Interconnect Network", "LIN-buss"],
        "exact_case": ["LIN"],
    },
    "Object Component Model/COM": {
        "any_case": ["Component Object Model", "Object Component Model"],
        "exact_case": ["COM"],
    },
    "REST": {
        "any_case": ["RESTful", "REST API", "REST-API"],
        "exact_case": ["REST"],
    },
    "RFID-teknik": {
        "any_case": ["RFID-teknik", "RFID"],
    },
    "XML Web Services": {
        "any_case": ["XML Web Services", "XML Web Service"],
    },
    "Ledningssystem (ISO 9000-serien)": {
        "any_case": [
            "ISO 9000",
            "ISO9000",
            "ISO 9001",
            "ISO9001",
            "ISO 9004",
            "ISO9004",
            "ISO 9000-serien",
            "ISO 9000 series",
        ],
    },
    "Quality Assurance (QA)": {
        "any_case": [
            "Quality Assurance",
            "kvalitetssäkring",
            "quality assurance engineer",
            "quality assurance specialist",
        ],
        "exact_case": ["QA"],
    },
    "ISO/IEC 20000": {
        "any_case": [
            "ISO/IEC 20000",
            "ISO IEC 20000",
            "ISO 20000",
            "ISO20000",
            "ISO/IEC 20000-1",
            "ISO 20000-1",
        ],
    },
    "ISO/IEC 25010": {
        "any_case": ["ISO/IEC 25010", "ISO IEC 25010", "ISO 25010", "ISO25010"],
    },
    "ISO/IEC 12207": {
        "any_case": [
            "ISO/IEC 12207",
            "ISO/IEC/IEEE 12207",
            "ISO IEC 12207",
            "ISO 12207",
            "ISO12207",
        ],
    },
    "ISO/IEC 330XX / SPICE": {
        "any_case": [
            "ISO/IEC 330",
            "ISO IEC 330",
            "ISO 330",
            "ISO/IEC 330xx",
            "ISO IEC 330xx",
            "Software Process Improvement and Capability Determination",
        ],
        "exact_case": ["SPICE"],
    },
    "3G-teknik": {
        "any_case": ["3G", "3G-teknik", "UMTS", "HSPA", "HSPA+"],
    },
    "4G-teknik": {
        "any_case": ["4G", "4G-teknik", "LTE", "LTE Advanced", "LTE-Advanced", "LTE-A"],
    },
    "5G-teknik": {
        "any_case": ["5G", "5G-teknik", "5G NR", "New Radio"],
        "exact_case": ["NR"],
    },
    "VoLTE": {
        "any_case": ["VoLTE", "Voice over LTE"],
    },
    "IMS": {"any_case": ["IP Multimedia Subsystem"], "exact_case": ["IMS"]},
    "Mobile Core / Core Network": {
        "any_case": [
            "Mobile Core",
            "Core Network",
            "Mobile Core Network",
            "mobilkärnnät",
            "kärnnät",
        ],
    },
    "RAN": {
        "any_case": ["Radio Access Network", "Radio Access Networks"],
        "exact_case": ["RAN"],
    },
    "eSIM": {
        "any_case": ["eSIM", "embedded SIM", "embedded SIM card"],
    },
    "Nätverksdesign": {
        "any_case": [
            "nätverksdesign",
            "network design",
            "design av nätverk",
            "nätverksarkitektur",
            "network architecture",
        ],
    },
    "Nätverksteknik": {
        "any_case": ["nätverksteknik", "network technology", "networking"],
    },
    "VLAN": {
        "any_case": ["Virtual LAN", "Virtual Local Area Network"],
        "exact_case": ["VLAN"],
    },
    "VPN": {"any_case": ["Virtual Private Network"], "exact_case": ["VPN"]},
    "WLAN / WiFi": {
        "any_case": [
            "Wi-Fi",
            "WiFi",
            "Wireless LAN",
            "Wireless Local Area Network",
            "trådlöst nätverk",
            "trådlösa nätverk",
        ],
        "exact_case": ["WLAN"],
    },
    "Routing & Switching": {
        "any_case": [
            "Routing & Switching",
            "Routing and Switching",
            "routing och switching",
            "routing/switching",
        ],
    },
    "SD-WAN": {
        "any_case": [
            "SD-WAN",
            "SD WAN",
            "Software-Defined WAN",
            "Software Defined WAN",
            "Software-Defined Wide Area Network",
            "Software Defined Wide Area Network",
        ],
    },
    "Microsoft Autopilot": {
        "any_case": ["Microsoft Autopilot", "Windows Autopilot"],
    },
    "Microsoft Intune": {
        "any_case": ["Microsoft Intune", "Intune"],
    },
    "Node": {
        "any_case": ["Node.js", "NodeJS", "Node js"],
        "exact_case": ["Node"],
    },
    "System Center Configuration Manager": {
        "any_case": [
            "System Center Configuration Manager",
            "Configuration Manager",
            "MECM",
            "MEMCM",
        ],
        "exact_case": ["SCCM"],
    },
    "Scrum": {
        "any_case": ["Scrum", "Scrum master"],
    },
    "Unified Modeling Language": {
        "any_case": ["Unified Modeling Language", "Unified Modelling Language"],
        "exact_case": ["UML"],
    },
    "Visual Studio Code": {
        "any_case": ["Visual Studio Code", "VS Code", "VSCode"],
    },
    "Visual Studio": {
        "any_case": ["Visual Studio", "MS Visual Studio", "Microsoft Visual Studio"],
    },
    "Windows Powershell": {
        "any_case": ["Windows Powershell", "Powershell"],
    },
    "Github": {
        "any_case": ["Github", "git hub"],
    },
    "Atlassian Jira": {
        "any_case": ["Atlassian Jira", "Jira Software", "Jira"],
    },
    "Enterprise JavaBeans": {
        "any_case": ["Enterprise JavaBeans"],
        "exact_case": ["EJB"],
    },
    "Java Persistence API": {
        "any_case": ["Java Persistence API"],
        "exact_case": ["JPA"],
    },
    "scikit-learn": {
        "any_case": ["scikit-learn", "sklearn", "scikit learn"],
    },
    ".NET": {
        "any_case": [".NET", "dotnet"],
    },
    "Entity Framework Core": {
        "any_case": ["Entity Framework Core", "EF Core", "Entity Framework"],
    },
    "Apache Hadoop": {
        "any_case": ["Apache Hadoop", "Hadoop"],
    },
    "Objektorienterad analys": {
        "any_case": ["Objektorienterad analys"],
        "exact_case": ["OOA"],
    },
    "Objektorienterad design": {
        "any_case": ["Objektorienterad design"],
        "exact_case": ["OOD"],
    },
    "Open Unified Process": {
        "any_case": ["Open Unified Process", "Open UP", "OpenUP"],
    },
    "Open Source": {
        "any_case": ["Open Source", "Öppen källkod", "Open-source", "opensource"],
        "exact_case": ["OSS"],
    },
    "Rational Rose": {
        "any_case": ["Rational Rose", "IBM Rational Rose"],
    },
    "Rational Unified Process": {
        "any_case": ["Rational Unified Process", "Unified Process"],
        "exact_case": ["RUP"],
    },
    "DevOps": {
        "any_case": ["DevOps", "dev ops", "dev-ops"],
    },
    "Extreme Programming": {
        "any_case": ["Extreme Programming", "extremprogramming", "extremprogrammering"],
        "exact_case": ["XP"],
    },
    "Test Driven Development": {
        "any_case": [
            "Test Driven Development",
            "Test-Driven Development",
            "testdriven utveckling",
            "testdriven systemutveckling",
        ],
        "exact_case": ["TDD"],
    },
    "Design Patterns": {
        "any_case": ["Design Patterns", "Designmönster", "Design pattern"],
    },
    "AIX": {
        "any_case": [
            "IBM AIX ",
            "AIX UNIX",
            "AIX-operativsystem",
            "AIX operativsystem",
            "AIX OS",
            "Advanced Interactive Executive",
        ],
    },
    "Amazon Linux": {
        "any_case": [
            "Amazon Linux2",
            "Amazon Linux 2",
            "Amazon Linux 2023",
            "Amazon Linux2023",
            "AWS Linux",
        ],
    },
    "Android": {
        "any_case": [
            "Android OS",
            "AndroidOS",
            "Android-operativsystem",
            "Android-plattform",
            "Android-system",
            "Android-kunnig",
        ],
    },
    "Arch Linux": {
        "any_case": ["ArchLinux", "Arch Linux OS", "Arch LinuxOS"],
    },
    "BlackBerry": {
        "any_case": [
            "BlackBerry OS",
            "BlackBerryOS",
            "BlackBerry-OS",
            "BlackBerry 10",
            "BlackBerry10",
            "BlackBerry-operativsystem",
            "BlackBerryoperativsystem",
            "BlackBerrysystem",
            "BlackBerry-plattform",
            "BlackBerryplattform",
        ],
    },
    "CentOS": {
        "any_case": [
            "CentOSLinux",
            "CentOS Linux",
            "CentOS Stream",
            "CentOSStream",
            "Community Enterprise Operating System",
            "Community Enterprise OS",
            "CommunityEnterpriseOS",
            "Community EnterpriseOS",
            "CommunityEnterprise OS",
            "Cent OS",
            "Cent-OS",
        ],
    },
    "DOS": {
        "any_case": [
            "MS-DOS",
            "MsDOS",
            "Microsoft DOS",
            "MicrosoftDOS",
            "Disk Operating System",
            "DiskOperatingSystem",
            "Disk OS",
        ],
    },
    "FreeBSD": {
        "any_case": [
            "Free BSD",
            "Free-BSD",
            "Free BSD Unix",
            "FreeBSD Unix",
            "Free-BSD Unix",
        ],
    },
    "Gentoo Linux": {
        "any_case": [
            "GentooLinux",
            "Gentoo/Linux",
            "Gentoo-Linux",
            "Gentoo",
            "Gentoo OS",
            "GentooOS",
            "Gentoo-OS",
        ],
    },
    "GNU": {
        "any_case": [
            "GNULinux",
            "GNU Linux",
            "GNU/Linux",
            "GNU-Linux",
            "GNU Operating System",
            "GNU-Operating System",
            "GNU OS",
            "GNU/OS",
            "GNUOS",
        ],
    },
    "iOS": {
        "any_case": [
            "iOS operativsystem",
            "iOS-operativsystem",
            "iOS-OS",
            "iOSOS",
            "iPhone OS",
            "iPhoneOS",
        ],
    },
    "IRIX": {
        "any_case": [
            "SGRI IRIX",
            "SGRIIRIX",
            "SGRI-IRIX",
            "SGRI/IRIX",
            "IRIX Unix",
            "IRIXUnix",
            "IRIX-Unix",
            "IRIX/Unix",
            "IRIS-baserat UNIX",
            "IRISbaserat UNIX",
            "IRIS/UNIX",
        ],
    },
    "JCL": {
        "any_case": [
            "IBM JCL",
            "IBMJCL",
            "IBM-JCL",
            "IBM/JCL",
            "Job Control Language",
            "JobControlLanguage",
            "Jobbkontrollspråk",
            "z/OS JCL",
            "z/OSJCL",
            "z/OS-JCL",
        ],
    },
    "Kali Linux": {
        "any_case": [
            "Kali-Linux",
            "KaliLinux",
            "Kali",
            "Kali Linux Operating System",
            "Kali Linux OS",
            "Kali LinuxOS",
            "KaliOS",
            "Kali-OS",
        ],
    },
    "Linux": {
        "any_case": [
            "Linuxsystem",
            "Linux-system",
            "Linux system",
            "Linuxbaserade system",
            "Linux-baserade system",
            "Linux-baserat system",
            "Linux-operativsystem",
            "Linux operativsystem",
            "Linux OS",
            "LinuxOS",
            "Linux/OS",
            "Linux-OS",
        ],
    },
    "Mac OS X": {
        "any_case": [
            "MacOS X",
            "MacOS-X",
            "Mac-OS X",
            "MacOSX",
            "OS X",
            "OS-X",
            "Mac OS",
            "MacOS",
            "Mac-OS",
        ],
    },
    "MVS": {
        "any_case": [
            "IBM MVS",
            "IBM-MVS",
            "IBM/MVS",
            "MVS/ESA",
            "MVS-ESA",
            "MVS ESA",
            "Multiple Virtual Storage",
        ],
    },
    "NetBSD": {
        "any_case": ["Net BSD", "Net-BSD"],
    },
    "NixOS": {
        "any_case": ["Nix OS", "Nix-OS", "Nix operating system"],
    },
    "openEuler": {
        "any_case": [
            "openEuler Linux",
            "openEulerLinux",
            "openEuler-Linux",
            "EulerOS",
            "Euler OS",
            "Euler Operating System",
        ],
    },
    "Oracle Linux": {
        "any_case": [
            "OracleLinux",
            "Oracle-Linux",
            "Oracle Enterprise Linux",
            "Oracle Linux Server",
        ],
        "exact_case": ["OEL"],
    },
    "OS/390": {
        "any_case": [
            "OS-390",
            "OS390",
            "OS 390",
            "IBM OS/390",
            "IBM-OS/390",
            "IBMOS/390",
            "Operating System/390",
            "Operating System390",
            "Operating System-390",
            "Operating System 390",
        ],
    },
    "OS/400": {
        "any_case": [
            "OS-400",
            "OS400",
            "OS 400",
            "IBM OS/400",
            "IBM-OS/400",
            "IBMOS/400",
            "Operating System/400",
            "Operating System400",
            "Operating System-400",
            "Operating System 400",
        ],
    },
    "OSE": {
        "any_case": [
            "Enea OSE",
            "OSE operating system",
            "OSE OS",
            "OSEOS",
            "OSE-OS",
            "OSE/OS",
            "Enea OSEck",
            "Operating System Embedded",
        ],
    },
    "pSOS": {
        "any_case": [
            "pSOS+",
            "pSOS OS",
            "pSOS operating system",
            "pSOS operativsystem",
            "Integrated Systems pSOS",
            "Integrated Systems-pSOS",
            "pSOS system",
            "pSOSsystem",
            "pSOS-system",
        ],
    },
    "Raspberry Pi OS": {
        "any_case": [
            "Raspberry Pi-OS",
            "Raspberry-Pi OS",
            "Raspbian",
            "RaspberryPi operating system",
            "Raspberry-Pi operating system",
            "Raspberry Pi operating system",
            "Raspberry Pi operativsystem",
            "Raspberry Pi-system",
        ],
    },
    "Red Hat Enterprise Linux (RHEL)": {
        "any_case": [
            "RHEL",
            "RedHat",
            "Red Hat Enterprise Linux",
            "Red Hat Linux",
            "RedHat Linux",
            "RedHatLinux",
        ],
    },
    "Rocky Linux": {
        "any_case": [
            "RockyLinux",
            "Rocky Linux OS",
            "RockyLinux OS",
            "Rocky Linux Operativsystem",
            "RockyLinux Operativsystem",
            "Rocky OS",
            "Rocky Operativsystem",
        ],
    },
    "Solaris": {
        "any_case": [
            "Oracle Solaris",
            "OracleSolaris",
            "Sun Solaris",
            "SunSolaris",
            "Solaris OS",
            "SolarisOS",
            "Solaris Operativsystem",
        ],
    },
    "Ubuntu": {
        "any_case": [
            "UbuntuLinux",
            "Ubuntu Linux",
            "Ubuntu Server",
            "UbuntuServer",
            "Ubuntu Desktop",
            "UbuntuDesktop",
            "Ubuntu-Desktop",
            "Ubuntusystem",
            "Ubuntu system",
            "Ubuntu-system",
        ],
    },
    "UNIX": {
        "any_case": [
            "UNIX OS",
            "UNIXOS",
            "UNIX-OS",
            "UNIX operativsystem",
            "UNIX-operativsystem",
            "UNIXoperativsystem",
            "Unix operating system",
            "Unix-operating system",
            "Unix/Linux",
            "Unix-Linux",
        ],
    },
    "VM/CMS": {
        "any_case": [
            "VM-CMS",
            "VM CMS",
            "IBM VM/CMS",
            "VM/370",
            "VM-370",
            "z/VM",
            "z-VM",
            "CMS",
            "Conversational Monitor System",
        ],
    },
    "VMS": {
        "any_case": [
            "OpenVMS",
            "VAX/VMS",
            "VAX-VMS",
            "DEC VMS",
            "DEC/VMS",
            "DEC-VMS",
            "Virtual Memory System",
        ],
    },
    "VSE": {
        "any_case": [
            "IBM VSE",
            "IBM-VSE",
            "IBM/VSE",
            "z/VSE",
            "z-VSE",
            "Virtual Storage Extended",
        ],
    },
    "VxWorks": {
        "any_case": [
            "Wind River VxWorks",
            "VxWorks RTOS",
            "VxWorks operating system",
            "VxWorks OS",
            "VxWorks operativsystem",
        ],
    },
    "Windows för mobila enheter": {
        "any_case": ["Windows mobile"],
    },
    "Windows Server": {
        "any_case": [
            "Microsoft Windows Server",
            "Windows Server 2019",
            "Windows Server 2022",
            "Windows Server 2025",
            "Windows-Server",
        ],
    },
    "Windows": {
        "any_case": [
            "Microsoft Windows",
            "Windows OS",
            "Windows/OS",
            "Windows-OS",
            "Windows operativsystem",
            "Windows operating system",
            "Windowssystem",
            "Windows 10",
            "Windows 11",
        ],
    },
    "Agile": {
        "any_case": [
            "Agilt",
            "agil",
            "Agilt arbetssätt",
            "Agila",
            "Agil metod",
            "Agila metoder",
            "Agila arbetsmetoder",
            "Agile method",
            "Agile methodology",
            "Agile ways of working",
        ],
    },
    "API-design": {
        "any_case": [
            "APIer",
            "API:er",
            "API-er",
            "API design",
            "design av API:er",
            "utforma API:er",
            "REST API design",
        ],
        "exact_case": ["API"],
    },
    "Artificial Intelligence / Artificiell intelligens / AI": {
        "any_case": [
            "Artificiell intelligens",
            "Artificial Intelligence",
            "AI-lösningar",
            "AI lösningar",
            "AI-utveckling",
            "AI utveckling",
            "AI system",
        ],
        "exact_case": ["AI"],
    },
    "Asset Information Management": {
        "any_case": [
            "asset information management systems",
            "asset information management system",
            "AIM system",
            "AIM-system",
            "AIM plattform",
            "AIM-plattform",
        ],
        "exact_case": ["AIM"],
    },
    "Automationsteknik": {
        "any_case": [
            "Automation",
            "Automatisering",
            "Industriell Automation",
            "Automation technology",
            "Automatiseringslösning",
            "Automatiseringslösningar",
        ],
    },
    "Blockkedjeteknik": {
        "any_case": [
            "blockchain",
            "block chain",
            "block-chain",
            "distributed ledger technology",
            "DLT",
            "Blockkedjelösning",
        ],
    },
    "Budgetansvar": {
        "any_case": [
            "Budgetansvarig",
            "budget management",
            "ansvar för budget",
            "budgetuppföljning",
            "budgetering",
        ],
    },
    "CASE-verktyg": {
        "any_case": [
            "CASE verktyg",
            "CASE tools",
            "CASE tool",
            "software engineering tools",
            "Computer-Aided Software Engineering",
        ],
        "exact_case": ["CASE"],
    },
    "Configuration Management / CM": {
        "any_case": [
            "Configuration Management",
            "konfigurationshantering",
            "konfiguration",
            "konfigurering",
            "konfigurationsstyrning",
            "software configuration management",
            "SCM",
            "Mjukvarukonfiguration",
        ],
        "exact_case": ["CM"],
    },
    "CORBA, distribuerad objektteknik": {
        "any_case": ["Common Object Request Broker Architecture"],
        "exact_case": ["CORBA"],
    },
    "Databasdesign": {
        "any_case": [
            "Database design",
            "design av databaser",
            "Databaslösning",
            "Databasschema",
            "Databasmodell",
            "Database model",
        ],
    },
    "Datamodellering": {
        "any_case": [
            "Datamodel",
            "Data modeling",
            "Databasmodellering",
            "Database modelling",
            "Datamodelsdesign",
            "Datamodel design",
            "Data model design",
        ],
    },
    "Dataskyddsförordningen / GDPR, erfarenhet": {
        "any_case": [
            "Dataskyddsförordningen",
            "General Data Protection Regulation",
            "GDPR compliance",
        ],
        "exact_case": ["GDPR"],
    },
    "Datawarehouse": {
        "any_case": [
            "Data warehouse",
            "Data warehousing",
            "Datalager",
            "enterprise data warehouse",
            "EDW",
        ],
    },
    "Design Thinking": {
        "any_case": [
            "Design Thinking-metod",
            "Design Thinking-metodik",
            "Design Thinking workshop",
            "Design-tänk",
            "designtänkande",
        ],
    },
    "Digitalisering": {
        "any_case": [
            "Digitalisering av processer",
            "Digital transformation",
            "Digital transformation initiatives",
        ],
    },
    "Distribuerad objektteknik": {
        "any_case": [
            "distributed object technology",
            "distributed objects",
            "distributed object systems",
        ],
    },
    "Dokumentation": {
        "any_case": [
            "Documentation",
            "Teknisk dokumentation",
            "Technical documentation",
            "Systemdokumentation",
        ],
    },
    "Driva workshops": {
        "any_case": ["Facilitera workshops", "leda workshops", "organisera workshops"],
    },
    "Engelska": {
        "any_case": ["English"],
    },
    "ERP-system, erfarenhet": {
        "any_case": [
            "ERP-system",
            "enterprise resource planning",
            "ERP-systems",
            "SAP ERP",
        ],
        "exact_case": ["ERP"],
    },
    "Felsökningsverktyg": {
        "any_case": [
            "Felsökning",
            "troubleshooting tools",
            "debugging tools",
            "diagnostic tools",
        ],
    },
    "Förändringsledning": {
        "any_case": ["Förändringsledarskap", "Change management", "Change leadership"],
    },
    "Geografiskt informationssystem / GIS": {
        "any_case": [
            "geografiskt informationssystem",
            "geographic information system",
            "geospatial information systems",
        ],
        "exact_case": ["GIS"],
    },
    "Git": {
        "any_case": ["versionshantering med Git", "Git repo", "Git version control"],
    },
    "Grafiska gränssnitt / GUI": {
        "any_case": [
            "graphical user interface",
            "grafiskt användargränssnitt",
            "grafiska gränssnitt",
            "graphical interfaces",
            "graphical user interfaces",
        ],
        "exact_case": ["GUI"],
    },
    "IANA/ICANN, bestämmelser och rekommendationer": {
        "any_case": [
            "Internet Assigned Numbers Authority",
            "Internet Corporation for Assigned Names and Numbers",
            "DNS governance",
            "internet standards",
            "bestämmelser och rekommendationer för internet",
        ],
        "exact_case": ["IANA", "ICANN"],
    },
    "Informatik": {
        "any_case": ["informatics", "informationssystem"],
    },
    "Informationsarkitektur": {
        "any_case": [
            "information architecture",
            "information architecture design",
            "design av informationsarkitektur",
        ],
        "exact_case": ["IA"],
    },
    "Informationsmodellering": {
        "any_case": [
            "information modelling",
            "information modeling",
            "informationsmodell",
            "informationsmodeller",
            "conceptual information model",
            "conceptual information modelling",
            "conceptual information modeling",
        ],
    },
    "Informationsstrategi": {
        "any_case": [
            "information strategy",
            "data strategy",
            "information management strategy",
            "strategi för informationshantering",
        ],
    },
    "Interaktionsdesign": {
        "any_case": [
            "interaction design",
            "UX interaction design",
            "design av interaktioner",
        ],
        "exact_case": ["IxD"],
    },
    "IT-konsultuppdrag, erfarenhet": {
        "any_case": [
            "IT-konsult",
            "IT-konsultuppdrag",
            "IT consulting",
            "IT consultant",
            "IT consultants",
            "konsultuppdrag inom IT",
            "IT consulting experience",
            "erfarenhet som IT-konsult",
        ],
    },
    "Kanban": {
        "any_case": [
            "Kanban-metodik",
            "Kanban-metoden",
            "Kanban board",
            "Kanban boards",
            "Kanban workflow",
            "Kanban metod",
            "Kanban-tavla",
            "Kanbantavla",
            "Kanban-tavlor",
        ],
    },
    "Kvalitetskontrollsystem, erfarenhet": {
        "any_case": [
            "kvalitetskontrollsystem",
            "quality control systems",
            "quality control system",
            "quality management system",
            "quality management systems",
            "quality assurance systems",
            "kvalitetsledningssystem",
            "erfarenhet av kvalitetskontrollsystem",
        ],
        "exact_case": ["QMS"],
    },
    "Länkad data": {
        "any_case": [
            "linked data",
            "Linked Open Data",
            "länkade data",
            "semantic web",
            "semantiska webben",
        ],
        "exact_case": ["LOD"],
    },
    "Ledning": {
        "any_case": [
            "leadership",
            "team leadership",
            "technical leadership",
            "leda team",
            "teamledning",
            "teknisk ledning",
        ],
    },
    "Machine learning / Maskininlärning": {
        "any_case": [
            "machine learning",
            "maskininlärning",
            "maskin inlärning",
            "machine learning model",
            "machine learning models",
            "machine learning algorithm",
            "machine learning algorithms",
            "maskininlärningsmodell",
            "maskininlärningsmodeller",
            "maskininlärningsalgoritmer",
        ],
        "exact_case": ["ML"],
    },
    "Människa-datorinteraktion / MDI": {
        "any_case": [
            "människa-datorinteraktion",
            "human-computer interaction",
            "human computer interaction",
            "user-computer interaction",
            "interaktion mellan människa och dator",
        ],
        "exact_case": ["HCI", "MDI"],
    },
    "Masterdata": {
        "any_case": [
            "master data",
            "master data management",
            "masterdatahantering",
            "hantering av masterdata",
        ],
        "exact_case": ["MDM"],
    },
    "Medieteknik": {
        "any_case": [
            "media technology",
            "digital media technology",
            "multimedia technology",
            "multimedieteknik",
        ],
    },
    "Model-view-viewmodel (MVVM)": {
        "any_case": [
            "Model View ViewModel",
            "Model-View-ViewModel",
            "Model View-ViewModel",
            "MVVM architecture",
            "MVVM pattern",
            "MVVM-arkitektur",
            "MVVM-mönster",
        ],
        "exact_case": ["MVVM"],
    },
    "Molnteknik": {
        "any_case": [
            "cloud technology",
            "cloud computing",
            "cloud infrastructure",
            "molnlösningar",
            "molninfrastruktur",
            "molnbaserade lösningar",
            "molnbaserade system",
        ],
    },
    "Objektorienterad metodik": {
        "any_case": [
            "object-oriented methodology",
            "object oriented methodology",
            "object-oriented design",
            "object oriented design",
            "object-oriented analysis and design",
            "object oriented analysis and design",
        ],
        "exact_case": ["OOAD"],
    },
    "OSL": {
        "any_case": [
            "offentlighets- och sekretesslagen",
            "offentlighets och sekretesslagen",
            "Offentlighets- och sekretesslag (2009:400)",
            "offentlighets- och sekretesslagstiftningen",
        ],
    },
    "Parallell programmering": {
        "any_case": [
            "parallel programming",
            "parallel computing",
            "concurrent programming",
            "multithreading",
            "flertrådad programmering",
            "parallell beräkning",
        ],
    },
    "pm3, förvaltningsmodell": {
        "any_case": [
            "förvaltningsmodellen pm3",
            "management model pm3",
            "pm3-modellen",
            "pm3 förvaltningsmodell",
        ],
        "exact_case": ["pm3", "pm³"],
    },
    "Praktisk ProjektStyrning / PPS": {
        "any_case": [
            "Praktisk ProjektStyrning",
            "PPS-modellen",
            "projektstyrningsmodell PPS",
            "projektstyrningsmodellen PPS",
        ],
        "exact_case": ["PPS"],
    },
    "Prediktiv analys": {
        "any_case": [
            "predictive analytics",
            "predictive analysis",
            "prediktiv modellering",
            "predictive modelling",
            "predictive modeling",
            "prediktiv dataanalys",
        ],
    },
    "Projektledning, IT": {
        "any_case": [
            "IT-projektledning",
            "IT project management",
            "projektledare IT",
            "IT project manager",
            "IT project managers",
            "projektledning inom IT",
            "projektledning av IT-projekt",
        ],
    },
    "PROPS, projektstyrningsmodell": {
        "any_case": [
            "PROPS-modellen",
            "Ericsson PROPS",
            "projektstyrningsmodell PROPS",
            "projektstyrningsmodellen PROPS",
        ],
        "exact_case": ["PROPS"],
    },
    "Säkerhetsanalys, datasäkerhet": {
        "any_case": [
            "säkerhetsanalys",
            "security analysis",
            "information security analysis",
            "data security",
            "security assessment",
            "analys av informationssäkerhet",
            "datasäkerhetsanalys",
            "bedömning av säkerhetsrisker",
        ],
    },
    "Scaled Agile Framework / SAFe": {
        "any_case": [
            "Scaled Agile Framework",
            "SAFe framework",
            "SAFe-metodik",
            "SAFe Agile",
            "Scaled Agile",
        ],
        "exact_case": ["SAFe"],
    },
    "Svenska": {
        "any_case": [
            "Swedish",
            "Swedish language",
            "modersmål svenska",
            "fluent Swedish",
            "flytande svenska",
            "goda kunskaper i svenska",
        ],
    },
    "Systemförvaltning": {
        "any_case": [
            "system management",
            "application management",
            "förvaltning av system",
            "förvaltning av applikationer",
            "applikationsförvaltning",
        ],
    },
    "Systemintegrering": {
        "any_case": [
            "system integration",
            "integration of systems",
            "integrationslösningar",
            "enterprise integration",
            "integrering av system",
            "integration mellan system",
        ],
    },
    "Systemutredning": {
        "any_case": [
            "systems analysis",
            "system investigation",
            "requirements analysis",
            "utredning av system",
        ],
    },
    "Telematik": {
        "any_case": [
            "telematics",
            "vehicle telematics",
            "telematiksystem",
            "fordonstelematik",
        ],
    },
    "Testautomatisering / Test automation": {
        "any_case": [
            "testautomatisering",
            "test automation",
            "automated testing",
            "automatiserade tester",
            "automated software testing",
            "automatisering av tester",
            "automatiserade programvarutester",
        ],
    },
    "Tjänsteorienterande arkitektur / SOA": {
        "any_case": [
            "service-oriented architecture",
            "service oriented architecture",
            "tjänsteorienterad arkitektur",
            "serviceorienterad arkitektur",
            "SOA architecture",
        ],
        "exact_case": ["SOA"],
    },
    "Verksamhetsanalys": {
        "any_case": [
            "business analysis",
            "business analyst",
            "business process analysis",
            "verksamhetsanalytiker",
            "analys av verksamhetsprocesser",
        ],
        "exact_case": ["BA"],
    },
    "WAP-teknik": {
        "any_case": ["Wireless Application Protocol", "WAP technology"],
        "exact_case": ["WAP"],
    },
    "Web Accessibility Initiative / WAI": {
        "any_case": ["Web Accessibility Initiative", "W3C WAI"],
        "exact_case": ["WAI"],
    },
    "Web Content Accessibility Guidelines / WCAG": {
        "any_case": [
            "Web Content Accessibility Guidelines",
            "WCAG compliance",
            "WCAG-kompatibilitet",
            "webbtillgänglighet",
        ],
        "exact_case": ["WCAG", "WCAG 2.1", "WCAG 2.2"],
    },
    "Webbutveckling": {
        "any_case": [
            "web development",
            "web developer",
            "web developers",
            "webbapplikationsutveckling",
            "frontend development",
            "backend development",
            "utveckling av webbapplikationer",
        ],
    },
}
