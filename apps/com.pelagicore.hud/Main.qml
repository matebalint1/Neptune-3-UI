/****************************************************************************
**
** Copyright (C) 2019 Luxoft Sweden AB
** Copyright (C) 2018 Pelagicore AG
** Contact: https://www.qt.io/licensing/
**
** This file is part of the Neptune 3 Cluster UI.
**
** $QT_BEGIN_LICENSE:GPL-QTAS$
** Commercial License Usage
** Licensees holding valid commercial Qt Automotive Suite licenses may use
** this file in accordance with the commercial license agreement provided
** with the Software or, alternatively, in accordance with the terms
** contained in a written agreement between you and The Qt Company.  For
** licensing terms and conditions see https://www.qt.io/terms-conditions.
** For further information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
** SPDX-License-Identifier: GPL-3.0
**
****************************************************************************/

import QtQuick 2.8
import QtQuick.Controls 2.2
import application.windows 1.0
import shared.Sizes 1.0
import "stores"
import "views"

NeptuneWindow {
    id: root

    width: Sizes.dp(480)
    height: Sizes.dp(240)

    property SurroundStore store: SurroundStore{}

    Button {
            id: button1
            text: "Surround View"
            font.pixelSize: 16

            property bool isSelected: true
            // property alias surroundView: SurroundStore.surroundView

            // signal surroundViewSelected(bool isSurround)

            anchors.centerIn: parent
            anchors.verticalCenterOffset: Sizes.dp(-60)
            anchors.rightMargin: Sizes.dp(20)
            width: Sizes.dp(150)
            height: Sizes.dp(50)
            onClicked: {
                console.log(`Button 1 clicked`)
                // root.store.setSurroundView(true)
                isSelected = true
                button2.isSelected = false
            }

            onIsSelectedChanged: {
                root.store.setSurroundView(isSelected)
            }

            background: Rectangle {
                color: button1.isSelected ? "green" : "black"
            }
        }

    Button {
            id: button2
            text: "Radar"
            font.pixelSize: 16

            property bool isSelected: false
            // property alias surroundView: SurroundStore.surroundView

            anchors.centerIn: parent
            anchors.verticalCenterOffset: Sizes.dp(+60)
            anchors.rightMargin: Sizes.dp(20)
            width: Sizes.dp(150)
            height: Sizes.dp(50)
            // radius: width / 2
            onClicked: {
                console.log(`Button 2 clicked`)
                // root.store.setSurroundView(false)
                isSelected = true
                button1.isSelected = false
            }

            background: Rectangle {
                color: button2.isSelected ? "green" : "black"
            }
        }
}

// Component.onCompleted: {
//     setWindowProperty("windowType", "hud");
// }

// MainView {
//     anchors.fill: parent
//     rootStore: RootStore {}
// }
