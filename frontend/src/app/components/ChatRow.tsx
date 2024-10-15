import Link from "next/link"
import { ChatBubbleLeftIcon } from "@heroicons/react/24/outline"
import { TrashIcon } from "@heroicons/react/16/solid"
import { usePathname, useRouter } from "next/navigation"
import { useEffect, useState } from "react"

type Props = {
    id:string
}


const ChatRow = ({id} : Props) => {
    const pathname = usePathname()
    const router   = useRouter()
    const [active, setActive] = useState(false)
    useEffect(()=>{
        if(!pathname) return;

        setActive(pathname.includes(id))   
    },[pathname]    
    )            

    const removeChat = async () => {
        router.replace("/")
    }

    return (  
        <div className="flex items-center" >      
        <div className="flex items-center justify-between w-40 overflow-hidden">
        <Link 
            href={`/chat/${id}`} 
            className={`chatRow flex items-center w-40 ${active && "bg-gray-700/50"}`}>
            <ChatBubbleLeftIcon className='h-5 w-5'/>
            <p className="flex-1 truncate">
                {id}
            </p>           
        </Link>  
        </div>
        <div>
         <TrashIcon 
         onClick={removeChat}
         className="h-5 w-5 text-gray-200 hover:text-red-700 flex-shrink-0"/> 
         </div>
         </div>      
  )

}

export default ChatRow