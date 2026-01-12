import { webSearchTool, fileSearchTool, Agent, RunContext, AgentInputItem, Runner, withTrace } from "@openai/agents";
import { z } from "zod";


// Tool definitions
const webSearchPreview = webSearchTool({
  filters: {
    allowed_domains: [
      "scholar.google.com"
    ]
  },
  searchContextSize: "medium",
  userLocation: {
    type: "approximate"
  }
})
const fileSearch = fileSearchTool([
  "vs_69647e1319748191b488beeb36081c86"
])
const webSearchPreview1 = webSearchTool({
  userLocation: {
    type: "approximate",
    country: undefined,
    region: undefined,
    city: undefined,
    timezone: undefined
  },
  searchContextSize: "medium"
})
const fileSearch1 = fileSearchTool([
  "vs_696480c04cf48191a431b1520a8ffc6f"
])
const ExtractProfessorInfoSchema = z.object({ Professor Name: z.string(), College Name: z.string(), Research Areas: z.string() });
const WriteEmailSchema = z.object({ Professor Name: z.string(), email id: z.string(), Email to Professor: z.string() });
const FundingAgentSchema = z.object({ Name of Professor: z.string(), email: z.string() });
const ClassifyAgentSchema = z.object({ Name of Professor: z.string(), College: z.string(), email id: z.string(), webpage: z.string() });
const extractProfessorInfo = new Agent({
  name: "Extract professor info",
  instructions: "You are a helpful assistant who extracts research areas and information of professors like name, college they teach in, and research areas. ",
  model: "gpt-4.1",
  tools: [
    webSearchPreview
  ],
  outputType: ExtractProfessorInfoSchema,
  modelSettings: {
    temperature: 1,
    topP: 1,
    maxTokens: 2048,
    store: true
  }
});

interface WriteEmailContext {
  inputOutputParsedEmail: string;
}
const writeEmailInstructions = (runContext: RunContext<WriteEmailContext>, _agent: Agent<WriteEmailContext>) => {
  const { inputOutputParsedEmail } = runContext.context;
  return `Write a formal email to the Professor inquiring about PhD admissions in June 2027. Explain my experience and convince him why I am a suitable candidate for PhD in his lab.  {{input.output_parsed.Name of Professor}} ${inputOutputParsedEmail}`
}
const writeEmail = new Agent({
  name: "Write Email",
  instructions: writeEmailInstructions,
  model: "gpt-4.1",
  tools: [
    fileSearch
  ],
  outputType: WriteEmailSchema,
  modelSettings: {
    temperature: 1,
    topP: 1,
    maxTokens: 2048,
    store: true
  }
});

interface FundingAgentContext {
  inputOutputParsedWebpage: string;
}
const fundingAgentInstructions = (runContext: RunContext<FundingAgentContext>, _agent: Agent<FundingAgentContext>) => {
  const { inputOutputParsedWebpage } = runContext.context;
  return `Check if the professors have funding to support their research and are actively looking for PhD students.  ${inputOutputParsedWebpage} {{input.output_parsed.Name of Professor}} {{input.output_parsed.College}} {{input.output_parsed.email id}}`
}
const fundingAgent = new Agent({
  name: "Funding Agent",
  instructions: fundingAgentInstructions,
  model: "gpt-4.1",
  tools: [
    webSearchPreview1
  ],
  outputType: FundingAgentSchema,
  modelSettings: {
    temperature: 1,
    topP: 1,
    maxTokens: 2048,
    store: true
  }
});

const classifyAgent = new Agent({
  name: "Classify Agent",
  instructions: "Is the professor doing research that is related to my areas of research ? If yes return the professor's name, college where they teach, webpage or website  and their email id {{input.output_parsed.Professor Name}}  {{input.output_parsed.College Name}} {{input.output_parsed.Research Areas}}",
  model: "gpt-4.1",
  tools: [
    fileSearch1,
    webSearchPreview1
  ],
  outputType: ClassifyAgentSchema,
  modelSettings: {
    temperature: 1,
    topP: 1,
    maxTokens: 2048,
    store: true
  }
});

type WorkflowInput = { input_as_text: string };


// Main code entrypoint
export const runWorkflow = async (workflow: WorkflowInput) => {
  return await withTrace("EmailProffPhd", async () => {
    const state = {

    };
    const conversationHistory: AgentInputItem[] = [
      { role: "user", content: [{ type: "input_text", text: workflow.input_as_text }] }
    ];
    const runner = new Runner({
      traceMetadata: {
        __trace_source__: "agent-builder",
        workflow_id: "wf_696478921d808190ad161cef7022bab00efa85288005f310"
      }
    });
    const extractProfessorInfoResultTemp = await runner.run(
      extractProfessorInfo,
      [
        ...conversationHistory
      ]
    );
    conversationHistory.push(...extractProfessorInfoResultTemp.newItems.map((item) => item.rawItem));

    if (!extractProfessorInfoResultTemp.finalOutput) {
        throw new Error("Agent result is undefined");
    }

    const extractProfessorInfoResult = {
      output_text: JSON.stringify(extractProfessorInfoResultTemp.finalOutput),
      output_parsed: extractProfessorInfoResultTemp.finalOutput
    };
    const classifyAgentResultTemp = await runner.run(
      classifyAgent,
      [
        ...conversationHistory
      ]
    );
    conversationHistory.push(...classifyAgentResultTemp.newItems.map((item) => item.rawItem));

    if (!classifyAgentResultTemp.finalOutput) {
        throw new Error("Agent result is undefined");
    }

    const classifyAgentResult = {
      output_text: JSON.stringify(classifyAgentResultTemp.finalOutput),
      output_parsed: classifyAgentResultTemp.finalOutput
    };
    const fundingAgentResultTemp = await runner.run(
      fundingAgent,
      [
        ...conversationHistory
      ],
      {
        context: {
          inputOutputParsedWebpage: classifyAgentResult.output_parsed.webpage
        }
      }
    );
    conversationHistory.push(...fundingAgentResultTemp.newItems.map((item) => item.rawItem));

    if (!fundingAgentResultTemp.finalOutput) {
        throw new Error("Agent result is undefined");
    }

    const fundingAgentResult = {
      output_text: JSON.stringify(fundingAgentResultTemp.finalOutput),
      output_parsed: fundingAgentResultTemp.finalOutput
    };
    const writeEmailResultTemp = await runner.run(
      writeEmail,
      [
        ...conversationHistory
      ],
      {
        context: {
          inputOutputParsedEmail: fundingAgentResult.output_parsed.email
        }
      }
    );
    conversationHistory.push(...writeEmailResultTemp.newItems.map((item) => item.rawItem));

    if (!writeEmailResultTemp.finalOutput) {
        throw new Error("Agent result is undefined");
    }

    const writeEmailResult = {
      output_text: JSON.stringify(writeEmailResultTemp.finalOutput),
      output_parsed: writeEmailResultTemp.finalOutput
    };
  });
}
