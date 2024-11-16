import logo from "../images/logo.svg"
import Image from "next/image"

export default function Header() {
    return (
        <header className="header-wrapper">
            <Image
             src={logo}
             alt="logo"
             className="logo-image"
             />
            <h2 className="pay-classification">Классификация назначения платежа</h2>
            <h3 className="team-name">Команда: Ekanam</h3>
        </header>
    )
}