# State Management Comparison — Redux Toolkit vs NgRx vs Pinia

Notes from building the same Student Portal enrollment/courses state three
times: Redux Toolkit here, Pinia in `handson_08`, and reading up on NgRx for
the Angular app in `handson_07` (which currently manages its state with
plain component state + services, not NgRx).

## Redux Toolkit (this project)

- State lives in slices (`enrollmentSlice.js`, `coursesSlice.js`), each a
  `createSlice` call producing a reducer + action creators.
- Async work goes through `createAsyncThunk` (`fetchAllCourses`), which
  auto-generates `pending`/`fulfilled`/`rejected` actions. `extraReducers`
  handles all three so loading/error state doesn't need to be hand-rolled.
- Components never touch `state.courses.courses` directly — they go through
  selectors (`selectCourses`, `selectCoursesLoading`) via `useSelector`.
  Reorganising the store shape later only means updating the selectors.
- Boilerplate is the lowest of the three once Redux Toolkit is in place —
  no action-type constants, no switch statements, Immer lets you "mutate"
  state in reducers safely.
- Learning curve: moderate. You need to understand the store/action/reducer
  flow and where thunks fit, but Redux Toolkit removes most of classic
  Redux's ceremony.

## NgRx (Angular)

- Same conceptual shape as Redux — Actions, Reducers, Selectors — plus
  Effects, which is the piece with no Redux Toolkit equivalent out of the
  box (Redux Toolkit's thunks are simpler but less powerful than Effects'
  RxJS-based operators).
- Data flow: Component → dispatch(Action) → Effect (intercepts the action,
  calls the API service, dispatches a new action with the result) → Reducer
  (pure function, updates state) → Selector → Component.
- Reducers must stay pure — no API calls or other side effects inside them.
  That's Effects' job, running outside the reducer entirely.
- Built-in tooling is the strongest of the three (schematics to generate
  actions/reducers/effects, Redux DevTools integration is automatic), but
  the file count and RxJS knowledge required push the learning curve higher
  than Redux Toolkit or Pinia.

## Pinia (Vue, `handson_08`)

- No actions/reducers split — a store is just reactive state (`ref`),
  computed getters, and functions that mutate that state directly
  (`enroll`, `unenroll` in `stores/enrollment.js`).
- Async logic is a plain `async` function in the store; no thunk middleware
  or effect layer needed, since Vue's reactivity system already tracks
  which components depend on which state.
- `storeToRefs(store)` is needed if you destructure store properties in
  `<script setup>` and want to keep reactivity — plain destructuring breaks
  it, since it copies the current value out of the reactive object.
- Boilerplate and learning curve are the lowest of the three — a Pinia
  store reads like a Vue composable, so anyone already comfortable with the
  Composition API can pick it up in minutes.

## Summary

| | Redux Toolkit | NgRx | Pinia |
|---|---|---|---|
| Boilerplate | Low | High | Lowest |
| Async pattern | `createAsyncThunk` | Effects (RxJS) | plain async functions |
| Learning curve | Moderate | Steepest | Gentlest |
| Built-in tooling | Redux DevTools | Redux DevTools + schematics | Vue DevTools |
