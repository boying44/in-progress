//
//  GameViewController.swift
//  FlappySnek
//
//  Created by OTSS on 8/28/17.
//  Copyright © 2017 OTSS. All rights reserved.
//

import UIKit
import SpriteKit
import GameplayKit

class GameViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        if let view = self.view as! SKView? {
            // Load the SKScene from 'GameScene.sks'
            if let scene = SKScene(fileNamed: "GameScene") {
                // Set the scale mode to scale to fit the window
                // print(scene.size) //defined in sks
                // print(self.view.frame.size) //defined by simulator
                scene.scaleMode = .aspectFill
                
                view.presentScene(scene)
            }
            
            view.ignoresSiblingOrder = true
            
            view.showsFPS = true
            view.showsNodeCount = true
            view.showsPhysics = true
        }
    }

    @IBAction func ChangeJumpHeight(_ sender: UISlider) {
        if let view = self.view as! SKView? {
            // Load the SKScene 0from 'GameScene.sks'
            if let scene = view.scene as! GameScene? {
                scene.changeVelocity(sender.value)
            }
        }
    }
    
    override var shouldAutorotate: Bool {
        return true
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Release any cached data, images, etc that aren't in use.
    }

    override var prefersStatusBarHidden: Bool {
        return true
    }
    
}
