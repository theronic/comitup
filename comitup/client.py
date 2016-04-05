#!/usr/bin/python

import dbus
import sys

bus = dbus.SystemBus()

try:
    ciu_service = bus.get_object(
                   'com.github.davesteele.comitup',
                   '/com/github/davesteele/comitup'
                  )
except dbus.exceptions.DBusException:
    print "Error connecting to the comitup D-Bus service"
    sys.exit(1)

ciu_state = ciu_service.get_dbus_method(
                'state',
                'com.github.davesteele.comitup'
            )
ciu_activity = ciu_service.get_dbus_method(
                'activity',
                'com.github.davesteele.comitup'
               )
ciu_points = ciu_service.get_dbus_method(
                'access_points',
                'com.github.davesteele.comitup'
             )
ciu_delete = ciu_service.get_dbus_method(
                'delete_connection',
                'com.github.davesteele.comitup'
             )
ciu_connect = ciu_service.get_dbus_method(
                'connect',
                'com.github.davesteele.comitup'
             )