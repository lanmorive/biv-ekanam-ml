"use client"
import { useEffect, useState, createRef } from "react";
import axios, {AxiosResponse} from "axios";
export default function MainForm() {
    const [answer, setAnswer] = useState("");
    const [inputValue, setInputValue] = useState("");
    const inputReference = createRef<HTMLInputElement>();
    async function getQueryToServer() {
        setInputValue(inputReference.current == undefined? "" : inputReference.current.value);
        console.log(inputValue);
    }
    useEffect(() => {
        axios.get(`http://localhost:8000/purpose_of_payment/${inputValue}`)
            .then((res: AxiosResponse) => setAnswer(res.data))
            .catch(error => {
                console.log(`error: ${error}`);
            })
    }, [inputValue])
    return (
        <div className="form-wrapper">
            <div className="top-part-form">
                <h3>Текст:</h3>
                <div className="input-and-btn">
                    <input type="text" ref={inputReference}/>
                    <button className="enter-btn" onClick={getQueryToServer}>Рассчитать</button>
                </div>
            </div>
            <div className="bottom-part-form">
                <h3>Результат:</h3>
                <div className="output-data">
                    <h3>{answer}</h3>
                </div>
            </div>
        </div>
    )
}