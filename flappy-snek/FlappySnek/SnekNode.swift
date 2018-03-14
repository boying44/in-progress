//
//  SnekNode.swift
//  FlappySnek
//
//  Created by OTSS  on 9/5/17.
//  Copyright © 2017 OTSS. All rights reserved.
//

import Foundation
import SpriteKit

class SnekNode: SKSpriteNode{

    private let length: Int
    private var segmentLocations: [CGPoint] = []
    private var vineSegments: [SKSpriteNode] = []
    
    init(length:Int, position:CGPoint){
        self.length = length
        super.init(texture: nil, color: .cyan, size: CGSize())
        
        self.position = position
        self.anchorPoint = CGPoint(x:1,y:1)
        self.name = name
    }

    //not sure what this does but is necessary
    required init?(coder aDecoder:NSCoder){
        self.length = 0
        super.init(coder: aDecoder)
    }
    
    func calculateSize() -> CGSize {
        var width = CGFloat(0)
        let height = (children[0] as! SKSpriteNode).size.height
        for child in children{
            if let child = child as? SKSpriteNode {
                width += child.size.width
            }
        }
        return CGSize(width: width, height:height)
    }
    
    func addToScene(_ scene: SKScene){
        zPosition = Layer.Vine
        scene.addChild(self)
        
        addHead(scene)
        
        //visualize origin
        let origin = SKShapeNode(circleOfRadius: 50)
        origin.strokeColor = .red
        addChild(origin)
    
        for i in 0..<length{
            print(i)
            let vineSegment = SKSpriteNode(imageNamed: "bodyStraight")
            let offset = vineSegment.size.width * CGFloat(i + 1)
            vineSegment.position = CGPoint(x: -offset, y: 0) //position in parent's coordinate system
            vineSegment.name = name
            vineSegment.anchorPoint = CGPoint(x:1, y:1)
            
            vineSegments.append(vineSegment)
            addChild(vineSegment)
        }
        self.size = calculateSize()
    }
    
    func addHead(_ scene: SKScene){
        let head = SKSpriteNode(imageNamed: "headStraight")
        head.position = CGPoint(x: 0, y: 0) //origin
        head.anchorPoint = CGPoint(x:1, y:1)

        addChild(head)
        

    }
}
