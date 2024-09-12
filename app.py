import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyDal7zcmQvQ4v_KM_ECRFIlkZw04Is6zpI"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
    st.markdown(
        """
            <div style ="text-align: center;
            color:red;">
                <h1> SQL Query Generator </h1>
                <h3>I can generate SQL queries for you! </h3>
                <h4>With Explanation as well!</h4>
                <p> This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
            </div>
        """,
        unsafe_allow_html=True
    )

    text_input = st.text_area("Enter your Query here in English")

    

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                Create a SQL query snippet using the below text:

                ```
                    {text_input}
                ```
                I just want a SQL query
            """
            formatted_template=template.format(text_input=text_input)
            response=model.generate_content(formatted_template)
            sql_query=response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")

            expected_output="""
                What would be the expected response of this SQL query Snippet:

                ```
                    {sql_query}
                ```
                Provide sample tabular Response with no Explanation
            """
            expected_output_formatted=expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            

            explanation="""
                Explain this SQL query:

                ```
                    {sql_query}
                ```
                Please provide with simplest of Explanation:
            """
            explanation_formatted= explanation.format(sql_query=sql_query)
            explanation=model.generate_content(explanation_formatted)
            explanation=explanation.text

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query:")
                st.code(sql_query, language="sql")
                st.success("Expected Output of this SQL Query will be:")
                st.markdown(eoutput)
                st.success("Explanation for this SQL Query:")
                st.markdown(explanation)


main()