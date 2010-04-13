/*
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 *
 * PathportDevice.h
 * Interface for the pathport device
 * Copyright (C) 2005-2009 Simon Newton
 */

#ifndef PLUGINS_PATHPORT_PATHPORTDEVICE_H_
#define PLUGINS_PATHPORT_PATHPORTDEVICE_H_

#include <string>
#include "olad/Device.h"
#include "ola/network/SelectServer.h"
#include "plugins/pathport/PathportNode.h"

namespace ola {
namespace plugin {
namespace pathport {

class PathportDevice: public ola::Device {
  public:
    PathportDevice(class PathportPlugin *owner,
                   const std::string &name,
                   class Preferences *preferences,
                   const class PluginAdaptor *plugin_adaptor);

    string DeviceId() const { return "1"; }
    PathportNode *GetNode() const { return m_node; }
    int SendArpReply();

    static const char K_DEFAULT_NODE_NAME[];
    static const char K_DSCP_KEY[];
    static const char K_NODE_ID_KEY[];
    static const char K_NODE_IP_KEY[];
    static const char K_NODE_NAME_KEY[];

  protected:
    bool StartHook();
    void PrePortStop();
    void PostPortStop();

  private:
    class Preferences *m_preferences;
    const class PluginAdaptor *m_plugin_adaptor;
    PathportNode *m_node;
    ola::network::timeout_id m_timeout_id;

    static const uint32_t PORTS_PER_DEVICE = 8;
    static const int ADVERTISTMENT_PERIOD_MS = 6000;
};
}  // pathport
}  // plugin
}  // ola
#endif  // PLUGINS_PATHPORT_PATHPORTDEVICE_H_
