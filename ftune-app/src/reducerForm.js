import React, { useReducer } from "react";

export default function ReducerForm() {
  const initialState = {
    firstName: "",
    lastName: "",
    bio: "",
    faveFruit: "",
  };

  const formReducer = (state, { type, payload }) => {
    // console.log(">>>>>state:", state, ", type:", type, ", payload:", payload);
    return { ...state, [type]: payload };
  };

  const [state, dispatch] = useReducer(formReducer, initialState);

  return (
    <form>
      <label>
        First Name:
        <input
          type="text"
          value={state.firstName}
          onChange={(event) =>
            dispatch({ type: "firstName", payload: event.target.value })
          }
        />
      </label>
      <label>
        Last Name:
        <input
          type="text"
          value={state.lastName}
          onChange={(event) =>
            dispatch({ type: "lastName", payload: event.target.value })
          }
        />
      </label>
      <label>
        Bio:
        <textarea
          value={state.bio}
          onChange={(event) =>
            dispatch({ type: "bio", payload: event.target.value })
          }
        />
      </label>
      <label>
        Favorite Fruit
        <select
          value={state.faveFruit}
          onChange={(event) =>
            dispatch({ type: "faveFruit", payload: event.target.value })
          }
        >
          <option value="pineapple">Pineapple 🍍</option>
          <option value="lemon">Lemon 🍋</option>
          <option selected value="coconut">
            Coconut 🥥
          </option>
          <option value="mango">Mango 🥭</option>
          <option value="strawberry">Strawberry 🍓</option>
          <option value="grapes">Grapes 🍇</option>
        </select>
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
}
