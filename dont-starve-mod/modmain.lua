-- if in the mod environment (modmain.lua), you need to get require from the global environment
local require = GLOBAL.require
-- -- Deployable becomes a reference to the cached result stored in package.loaded["components/deployable"]
-- local Deployable = require "components/deployable"
-- -- Store the existing function if it exists, otherwise store a dummy function as a fail-safe
-- local Deployable_CanDeploy_base = Deployable.CanDeploy or function() return true endfunction Deployable:CanDeploy( pt )
-- -- Get the result of the base CanDeploy function
-- -- Note: Deployable_CanDeploy_base is called with the self parameter because x:fn() is simply a shortcut for x.fn(x) with an implied self parameter
-- local can_deploy = Deployable_CanDeploy_base( self, pt )
-- -- Add in our own deployment requirement	
-- can_deploy = can_deploy and pt == GLOBAL.Point(0,0,0)	return can_deployend

--special post-init function for a particular prefab: pigs in this case
function pigmanpostinit(inst)
	print("hello pigman init!")

	--halve wilson's max hunger on initialization
	inst.components.health:SetMaxHealth(TUNING.PIG_HEALTH*0.5)

	--add your own component, defined in mods/[yourmodname]/scripts/components/myowncomponent.lua
	inst:AddComponent("myowncomponent")
end

function inventorypostinit(component,inst)
	print("hello inventory init!")
end

function simpostinit(player)
	print("hello sim init!")
	print("We are playing as "..player.prefab)
end

function gamepostinit()
	print("hello game init!")
	--if you want to load your own prefabs, this is where you'd do it
end

--add a post init for the pigman
AddPrefabPostInit("pigman", pigmanpostinit)

--add a post init function for the inventory component
AddComponentPostInit("inventory", inventorypostinit)

--add a post init to the sim starting up
AddSimPostInit(simpostinit)

--add a post init to the game starting up
AddGamePostInit(gamepostinit)

--override specific tuning values here!
TUNING.WILSON_HUNGER = 50

GLOBAL.CHEATS_ENABLED = true

GLOBAL.require( 'debugkeys' )