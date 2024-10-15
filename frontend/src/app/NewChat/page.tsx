'use client'


import { useRouter } from "next/navigation"
import { PlusIcon } from "@heroicons/react/16/solid"



const Newchat = () => {
    const router = useRouter()

    const createNewChat = async() => {  
        router.push(`/chat/one`)


    }
    return (
        <div onClick={createNewChat} className="border-gray-700 border chatRow">
           <PlusIcon className="h-4 w-4"/>
            <p>New chat</p>
        </div>
      )
    }
    
    export default Newchat    