//
//  Constants.swift
//  FlappySnek
//
//  Created by OTSS  on 9/6/17.
//  Copyright © 2017 OTSS. All rights reserved.
//

import Foundation
import SpriteKit

struct Layer {
    static let Background: CGFloat = 0
    static let Crocodile: CGFloat = 1
    static let Vine: CGFloat = 1
    static let Prize: CGFloat = 2
    static let Foreground: CGFloat = 3
}

struct PhysicsCategory {
    static let None: UInt32 = 0
    static let Pipe: UInt32 = 1
    static let Snek: UInt32 = 2
    static let Vine: UInt32 = 4
    static let Prize: UInt32 = 8
}
