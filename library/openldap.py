from ldap3 import Server, Connection


ldap_server = 'ldap://192.168.1.28:389'
ldap_user = 'cn=admin,dc=acaiblog,dc=top'
ldap_password = '123456'


server = Server(ldap_server)
conn = Connection(server, user=ldap_user, password=ldap_password)


if conn.bind():
    print("Successfully connected to LDAP server")

    result = conn.search(search_base='', search_filter='(objectClass=domain)',
                         attributes=['dc'])
    print "result: {}".format(result)
    if result:
        domain_controller_info = conn.entries[0]
        dc = domain_controller_info['dc'].value
        print("Domain Controller:", dc)
else:
    print("Connection to LDAP server failed:", conn.last_error)
