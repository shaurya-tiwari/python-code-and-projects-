import streamlit as st

st.title("Hello Streamlit!")


def gettask():
    tasks = []
    with open("data.txt") as datafile:
        for item in datafile:
            item = item.strip()
            if item:
                tasks.append(item)
    return tasks


tasks = gettask()

st.subheader("your tasks")
for task in tasks:
    st.checkbox(task)

st.subheader("ADD NEW TASK")
newtask = st.text_input("entter task here ")


if st.button("add task"):
    if newtask:
        with open("data.txt", "a") as datafile:
            datafile.write(newtask + "\n")
        st.success(f"task aded successfuly {newtask}")
        st.rerun()
    else:
        st.warning("enter valid task ")

st.subheader("remove task")
if tasks:
    removetask = st.selectbox("cchek box to remove task ", tasks)
    if st.button("remoe taks "):
        tasks.remove(removetask)
        with open("data.txt", "w") as datafile:
            for task in tasks:
                datafile.write(task + "\n")
        st.success("task remove suceess ")
        st.rerun()
else:
    st.info("no task to remoe ")
