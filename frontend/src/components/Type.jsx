function Type( {type} ) {

    const typeEmojis = {
            fire: "🔥",
            water: "💧",
            grass: "🌿",
            electric: "⚡",
            ice: "❄️",
            fighting: "🥊",
            poison: "☠️",
            ground: "🌍",
            flying: "🕊️",
            psychic: "🔮",
            bug: "🐛",
            rock: "🪨",
            ghost: "👻",
            dragon: "🐉",
            dark: "🌑",
            steel: "⚙️",
            fairy: "✨",
            normal: "⭐"
        };

    return (
        <div>
        {type} {typeEmojis[type.toLowerCase()]}
        </div>
    )

}

export default Type