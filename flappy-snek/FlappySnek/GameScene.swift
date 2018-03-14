//
//  GameScene.swift
//  FlappySnek
//
//  Created by OTSS on 8/28/17.
//  Copyright © 2017 OTSS. All rights reserved.
//

import SpriteKit
import GameplayKit

class GameScene: SKScene , SKPhysicsContactDelegate{
    
    let pipeArray = ["uppipe1", "downpipe1"]
    var snek: SnekNode!
    var jumpHeight: Int = 900
    
    override func didMove(to view: SKView) {
        physicsWorld.gravity = CGVector(dx:0.0, dy:-9.8)
        physicsWorld.speed = 0.5
        physicsWorld.contactDelegate = self
        
        snek = SnekNode(length: 1, position: CGPoint(x: size.width*0.3, y: size.height))
        
        snek.addToScene(self)
        
        let physicsBodyCenter = CGPoint(x: -snek.size.width/2, y: -snek.size.height/2) //position of snake is top right, physics body is centered by center
        snek.physicsBody = SKPhysicsBody(rectangleOf: snek.size, center: physicsBodyCenter)
        snek.physicsBody?.isDynamic = true
        snek.physicsBody?.categoryBitMask = PhysicsCategory.Snek
        snek.physicsBody?.contactTestBitMask = PhysicsCategory.Pipe
        snek.physicsBody?.collisionBitMask = PhysicsCategory.None
        snek.physicsBody?.affectedByGravity = true
        
        run(SKAction.repeatForever(
            SKAction.sequence([
                SKAction.run(addPipe),
                SKAction.wait(forDuration: 2.0) // TODO: make random
                ])
        ))
    }
    
    func changeVelocity(_ change: Float){
        jumpHeight = 900 + Int(change)
    }
    
    func addPipe(){
        let randomIndex = Int(arc4random_uniform(UInt32(pipeArray.count)))
        let pipe = SKSpriteNode(imageNamed: pipeArray[randomIndex])
        
        pipe.physicsBody = SKPhysicsBody(rectangleOf: pipe.size)
        pipe.physicsBody?.isDynamic = true
        pipe.physicsBody?.categoryBitMask = PhysicsCategory.Pipe
        pipe.physicsBody?.contactTestBitMask = PhysicsCategory.Snek
        pipe.physicsBody?.collisionBitMask = PhysicsCategory.None
        pipe.physicsBody?.affectedByGravity = false
        
        // Y position depending on up or down
        var actualY: CGFloat
        if randomIndex == 0 {
            actualY = size.height - pipe.size.height/2
        }
        else {
            actualY = pipe.size.height/2
        }
        
        pipe.position = CGPoint(x: size.width - pipe.size.width, y: actualY)
        addChild(pipe)
        
        let actualDuration = CGFloat(4.0)
        let actionMove = SKAction.move(to: CGPoint(x: -pipe.size.width/2, y: actualY), duration: TimeInterval(actualDuration))
        
        let actionMoveDone = SKAction.removeFromParent()
        pipe.run(SKAction.sequence([actionMove,actionMoveDone]))
    }
    
    /// must be edited
    func snekDidCollideWithPipe(pipe: SKSpriteNode, snek: SKSpriteNode) {
        print("Hit")
        //snek.removeFromParent()
    }
    
    func didBegin(_ contact: SKPhysicsContact) {
        
        // 1
        var firstBody: SKPhysicsBody
        var secondBody: SKPhysicsBody
        if contact.bodyA.categoryBitMask < contact.bodyB.categoryBitMask {
            firstBody = contact.bodyA
            secondBody = contact.bodyB
        } else {
            firstBody = contact.bodyB
            secondBody = contact.bodyA
        }
        
        // dangerous stuff
        let p = firstBody.node as! SKSpriteNode
        let pbox = SKShapeNode(rect: CGRect(x:p.position.x - p.size.width/2, y:p.position.y - p.size.height/2, width: p.size.width, height: p.size.height)) //magic to draw it in the right place since the SKShape is drawn at lower left corner
        pbox.strokeColor = .green
        addChild(pbox)
        
        let s = secondBody.node as! SKSpriteNode
        addChild(SKShapeNode(rect: CGRect(x:s.position.x - s.size.width, y:s.position.y - s.size.height, width: s.size.width, height: s.size.height))) //snek is anchored at upper right so subtract heigth and wifth for lower left
        //
        
        if ((firstBody.categoryBitMask & PhysicsCategory.Pipe != 0) &&
            (secondBody.categoryBitMask & PhysicsCategory.Snek != 0)) {
            if let pipe = firstBody.node as? SKSpriteNode, let
                snek = secondBody.node as? SKSpriteNode {
                snekDidCollideWithPipe(pipe: pipe, snek: snek)
            }
        }
        
    }
    
    
    //pls make the logic better
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first else {
            return
        }
        let touchLocation = touch.location(in: self)
        
        snek.physicsBody?.velocity = CGVector(dx: 0, dy: jumpHeight)
    }
    
}
